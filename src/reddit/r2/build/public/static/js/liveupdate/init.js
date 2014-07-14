!function(r, Backbone, $, _) {
  'use strict'

  var exports = r.liveupdate = {}

  var PermissionSet = function(permissions) {
    this._permissions = permissions
  }
  _.extend(PermissionSet.prototype, {
    isSuperUser: function() {
      return !!this._permissions.all
    },

    allow: function(name) {
      if (this.isSuperUser()) {
        return true
      }

      return _.has(this._permissions, name)
    },
  })

  exports.LiveUpdateApp = function() {
    var $header = $('.content > header')
    var $options = $('<div id="liveupdate-options">')

    this.permissions = new PermissionSet(r.config.liveupdate_permissions)

    this.event = new r.liveupdate.event.LiveUpdateEvent()
    this.eventView = new r.liveupdate.event.LiveUpdateEventView({
      model: this.event,
    })
    this.statusBarView = new r.liveupdate.statusBar.StatusBarView({
      model: this.event,
      el: $('#liveupdate-statusbar'),
    })
    this.event.fetch()  // bootstrap from preload

    this.listing = new r.liveupdate.listings.LiveUpdateListing()
    this.listingView = new r.liveupdate.listings.LiveUpdateListingView({
      model: this.listing,
      permissions: this.permissions,
    })
    this.listing.fetch({reset: true})  // bootstrap from preload

    this.embedViewer = new r.liveupdate.embeds.EmbedViewer({
      model: this.listing,
      el: this.listingView.el,
    })
    this.embedViewer.start()

    if (r.config.liveupdate_websocket) {
      this.websocket = new r.WebSocket(r.config.liveupdate_websocket)

      this.websocket.on({
        'connecting': function() {
          this.event.set('socket_state', 'connecting')
        },
        'connected': function() {
          this.event.set('socket_state', 'connected')
        },
        'disconnected': function() {
          this.event.set('socket_state', 'disconnected')
        },
        'reconnecting': function(delay) {
          this.event.set({
            'socket_state': 'reconnecting',
            'reconnect_delay': delay,
          })
        },
        'message:activity': function(message) {
          this.event.set({
            'viewer_count': message.count,
            'viewer_count_fuzzed': message.fuzzed,
          })
        },
        'message:settings': function(updates) {
          this.event.set(updates)
        },
        'message:update': function(update) {
          var attributes = r.liveupdate.listings.LiveUpdate.prototype.parse(update)
          this.listing.add(attributes, {at: 0})
        },
        'message:delete': function(updateId) {
          this.listing.remove(updateId)
        },
        'message:strike': function(updateId) {
          var stricken = this.listing.get(updateId)
          stricken.set('stricken', true)
        },
        'message:embeds_ready': function(data) {
          var model = this.listing.get(data.liveupdate_id)
          model.set('embeds', data.media_embeds)
          this.embedViewer.restart()
        },
        'message:complete': function() {
          this.event.set('state', 'complete')
          $options.remove()
          $('#new-update-form').remove()
        },
      }, this)

      if ('Notification' in window && !$('body').hasClass('embed')) {
        this.desktopNotifier = new r.liveupdate.notifications.DesktopNotifier({
          model: this.listing,
        })
        this.desktopNotifier.render()
        $('<label>')
          .text(r._('popup notifications'))
          .prepend(this.desktopNotifier.$el)
          .appendTo($options)
      }

      this.websocket.start()
    }

    this.activityTracker = new r.liveupdate.activity.ActivityTracker()
    this.faviconUpdater = new r.liveupdate.favicon.UnreadUpdateCounter({
      model: this.listing,
    })

    $options.insertAfter($header)
  }
}(r, Backbone, jQuery, _)


$(function() {
  'use strict'

  if ($('body').hasClass('liveupdate-event')) {
    r.liveupdate.app = new r.liveupdate.LiveUpdateApp()
  }
})
