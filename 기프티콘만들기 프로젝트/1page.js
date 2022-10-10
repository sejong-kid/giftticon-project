const data = 'data';

const aTag = document.querySelector('inputarea');
aTag.addEventListener('click', () => {
  location.href = `2page.html?${data}`;
});
