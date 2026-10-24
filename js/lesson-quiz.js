/* Lesson quizzes: progressive enhancement.
 * The build renders each quiz with the answer marked (so the page still works without JavaScript).
 * With JavaScript, the answer and explanation stay hidden until the reader picks an option. */
(function () {
  'use strict';
  var CARD = '.gazette-quiz-card';

  function reset(card) {
    var opts = card.querySelectorAll('.quiz-option-btn');
    opts.forEach(function (btn) {
      var icon = btn.querySelector('span');
      if (icon) icon.textContent = '⚪';
      if (btn.classList.contains('correct-option')) btn.setAttribute('data-correct', 'true');
      btn.classList.remove('correct-option');
      btn.removeAttribute('aria-disabled');
    });
    var ex = card.querySelector('.quiz-explanation');
    if (ex) { ex.hidden = true; ex.setAttribute('role', 'status'); }
    card.setAttribute('data-quiz-ready', 'true');
    card.removeAttribute('data-answered');
  }

  function answer(btn) {
    var card = btn.closest(CARD);
    if (!card || card.hasAttribute('data-answered')) return;
    card.setAttribute('data-answered', 'true');
    var chosenIsRight = btn.getAttribute('data-correct') === 'true';
    card.querySelectorAll('.quiz-option-btn').forEach(function (o) {
      var icon = o.querySelector('span');
      o.setAttribute('aria-disabled', 'true');
      if (o.getAttribute('data-correct') === 'true') {
        o.classList.add('correct-option');
        if (icon) icon.textContent = '✅';
      } else if (o === btn) {
        o.classList.add('wrong-option');
        if (icon) icon.textContent = '❌';
      }
    });
    var ex = card.querySelector('.quiz-explanation');
    if (ex) {
      ex.hidden = false;
      var lead = document.createElement('strong');
      lead.textContent = chosenIsRight ? '✓ ' : '✗ ';
      if (!ex.querySelector('strong[data-lead]')) { lead.setAttribute('data-lead', ''); ex.insertBefore(lead, ex.firstChild); }
    }
  }

  function init() {
    document.querySelectorAll(CARD).forEach(function (c) { if (!c.hasAttribute('data-quiz-ready')) reset(c); });
    // Delegated, so it keeps working when the flipbook moves pages around.
    document.addEventListener('click', function (e) {
      var btn = e.target.closest && e.target.closest('.quiz-option-btn');
      if (btn && btn.closest(CARD)) answer(btn);
    });
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
