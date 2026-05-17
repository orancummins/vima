/* eslint-disable no-undef */
document.addEventListener('sonicCompletion', onCompletion);


// eslint-disable-next-line no-unused-vars
function replayDemo() {
    let confirmOrderStep = document.getElementById('confirmOrderStep');
    let animationStep = document.getElementById('animationStep');
    let replayDemoStep = document.getElementById('replayDemoStep');

    confirmOrderStep.classList.remove('hide');
    animationStep.classList.add('hide');
    replayDemoStep.classList.add('hide');

    window.scrollTo({ top: 0, behavior: 'auto' });
}

// eslint-disable-next-line no-unused-vars
function pay() {
    let loaderText = document.getElementById('spinnerText');
    let loaderContainer = document.getElementById('loaderContainer');

    loaderText.innerHTML = 'Transaction is processing...';
    loaderContainer.classList.remove('hide');

    setTimeout(() => {
        loaderText.innerHTML = 'Transaction successful...';
        setTimeout(() => {
            loaderContainer.classList.add('hide');
            onPaySuccess();
        }, 2000);
    }, 2000);
}

function onPaySuccess() {
    let confirmOrderStep = document.getElementById('confirmOrderStep');
    let animationStep = document.getElementById('animationStep');

    animationStep.classList.remove('hide');
    confirmOrderStep.classList.add('hide');
    window.scrollTo({ top: 0, behavior: 'auto' });

    let cardType = document.getElementById('cardSelector').value;

    if (cardType === 'mastercard') {
        let el = document.getElementById('mc-sonic');
        el.play();
    } else {
        onCompletion();
    }
}

function onCompletion() {
    console.log('Completed');

    let animationStep = document.getElementById('animationStep');
    let replayDemoStep = document.getElementById('replayDemoStep');

    replayDemoStep.classList.remove('hide');
    animationStep.classList.add('hide');
    window.scrollTo({ top: 0, behavior: 'auto' });
}

// Keep startup lightweight: use native select and avoid external jquery dependency.
document.addEventListener('DOMContentLoaded', function() {
    var btn = document.querySelector('.pay-button');
    if (btn) btn.removeAttribute('disabled');
});
