!function(r, Backbone, $, _) {
  'use strict'

  var exports = r.liveupdate.statusBar = {}

  var Countdown = function(tickCallback, delay) {
    this._tickCallback = tickCallback
    this._deadline = Date.now() + delay
    this._interval = setInterval(_.bind(this._onTick, this), 1000)

    this._onTick()
  }
  _.extend(Countdown.prototype, {
    cancel: function() {
      if (this._interval) {
        clearInterval(this._interval)
        this._interval = null
      }
    },

    _onTick: function() {
      var delayRemaining = this._deadline - Date.now()
      var delayInSeconds = Math.round(delayRemaining / 1000)

      if (delayInSeconds >= 1) {
        this._tickCallback(delayInSeconds)
      } else {
        this.cancel()
      }
    },
  })

  exports.StatusBarView = Backbone.View.extend({
    tagName: 'div',
    className: 'status-bar',

    initialize: function() {
      this.listenTo(this.model, {
        'change:state change:delay_remaining': this.renderState,
        'change:socket_state': this.onSocketStateChange,
        'change:viewer_count': this.renderViewerCount,
      })
    },

    _stateText: function() {
      var delay

      switch (this.model.get('state')) {
      case 'complete':
        return {
          text: r._('no further updates'),
        }
      case 'live':
        switch (this.model.get('socket_state')) {
        case 'connecting':
          return {
            text: r._('connecting'),
            titleText: r._('connecting to update server'),
          }
        case 'connected':
          return {
            text: r._('live'),
            titleText: r._('updating in real time'),
          }
        case 'disconnected':
          return {
            text: r._('could not connect to update servers. please refresh'),
          }
        case 'reconnecting':
          delay = this.model.get('delay_remaining')
          return {
            text: r.P_(
              'disconnected. retrying in %(delay)s second...',
              'disconnected. retrying in %(delay)s seconds...',
              delay
            ).format({'delay': delay})
          }
        }
      }
    },

    onSocketStateChange: function() {
      var _this = this
      var socketState = this.model.get('socket_state')
      if (socketState === 'reconnecting') {
        this._reconnectCountdown = new Countdown(function(remaining) {
          _this.model.set('delay_remaining', remaining)
        }, this.model.get('reconnect_delay'))
      } else {
        if (this._reconnectCountdown) {
          this._reconnectCountdown.cancel()
          this._reconnectCountdown = null
        }
        this.renderState()
      }
    },

    renderState: function() {
      var classes = [
        this.className,
        this.model.get('state'),
        this.model.get('socket_state'),
      ]
      var $state = this.$('.state')
      var stateText = this._stateText()

      this.$el.attr('class', classes.join(' '))

      $state
        .text(stateText.text)
        .attr('title', stateText.titleText || '')

      return this
    },

    renderViewerCount: function() {
      var $viewerCount = this.$viewerCount || $('<p class="viewer-count">')

      var viewerCount = this.model.get('viewer_count')
      var viewerString = r.P_('%(num)s viewer', '%(num)s viewers', viewerCount)
      var viewerCountPrefix = this.model.get('viewer_count_fuzzed') ? '~' : ''

      $viewerCount
        .text(viewerString.format({num: viewerCountPrefix + viewerCount}))

      if (!this.$viewerCount) {
        this.$viewerCount = $viewerCount
        this.$el.append($viewerCount)
      }

      return this
    },
  })
}(r, Backbone, jQuery, _)
