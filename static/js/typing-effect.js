document.addEventListener('DOMContentLoaded', function() {
    const messages = [
        'hi',
        'hello',
        'hola',
        'just-saying-hi',
        'remember, you are amazing',
        'this blog is inspired by Hugo Ivy theme',
        'wanna chat ?',
        'reach me on linkedin',
        'else',
        'reach me on alad (at) terpmail (dot) umd (dot) edu',
        'trying to dodge the bots',
        'if you did not catch that',
        'thanks for stopping buy'
    ];

    let idx = 0;
    let charIdx = 0;
    const delay = 100; // typing speed in ms
    const hold = 1000; // pause after each message in ms

    const typingEffect = document.getElementById('typing-effect');

    function type() {
        const currentMessage = messages[idx];
        if (charIdx < currentMessage.length) {
            typingEffect.textContent += currentMessage.charAt(charIdx);
            charIdx++;
            setTimeout(type, delay);
        } else {
            setTimeout(() => {
                typingEffect.textContent = '';
                idx = (idx + 1) % messages.length;
                charIdx = 0;
                type();
            }, hold);
        }
    }

    type(); // Start typing effect
});
