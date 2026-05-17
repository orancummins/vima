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

/* Custom select design */
// eslint-disable-next-line no-undef
jQuery().ready(function() {

    $('.pay-button').removeAttr('disabled');

    $('.drop-down').append('<div class="button"></div>');
    $('.drop-down').append('<ul class="select-list"></ul>');
    $('.drop-down select option').each(function() {
        var background = $(this).css('background-image');
        $('.select-list').append('<li class="clsAnchor"><span value="' + $(this).val() + '" class="' + $(this).attr('class') +
            '" style=background-size:50px;background-image:' + background + '><p class="masking">.... </p>' + $(this).text() + '</span></li>');
    });
    $('.drop-down .button').html('<span class="card-image" style=background-image:' + $('.drop-down select').find(':selected').css('background-image') +
        ';><p class="masking">.... </p>' + $('.drop-down select').find(':selected').text() + '</span>' +
        '<a href="javascript:void(0);" class="select-list-link">' +
        '<img class="drop-down-icon" src="./assets/img/down.png"/></a>');
    $('.drop-down ul li').each(function() {
        if ($(this).find('span').text() == $('.drop-down select').find(':selected').text()) {
            $(this).addClass('active');
        }
    });
    $('.drop-down .select-list span').on('click', function() {
        var dropdown_text = $(this).text().replace('.... ', '');
        var dropdown_img = $(this).css('background-image');
        var dropdown_val = $(this).attr('value');
        $('.drop-down .button').html('<span class="card-image" style=background-image:' + dropdown_img + ';><p class="masking">.... </p>' +
            dropdown_text + '</span>' + '<a href="javascript:void(0);" class="select-list-link">' +
            '<img class="drop-down-icon" src="./assets/img/down.png"/></a>');
        $('.drop-down .select-list span').parent().removeClass('active');
        $(this).parent().addClass('active');
        $('.drop-down select[name=options]').val(dropdown_val);
        $('.drop-down .select-list li').slideUp(300);
    });
    $('.drop-down .button').on('click', function() {
        $('.drop-down ul li').slideToggle(300);
    });
});
/* End */
