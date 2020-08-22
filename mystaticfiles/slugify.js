const titleInput = document.querySelector('input[name=title]');
const slugInput = document.querySelector('input[name=slug]');

const slugify =(val) => {
  return val.toString().toLowerCase().trim()
    .replace(/&/g, '-and-')  //to replace '&' with '-and-'
    .replace(/[\s\W-]+/g,'-') // to replace, non-wordcharacters and dashes with a single dash
};

titleInput.addEventListener('keyup',(e) => {
  slugInput.setAttribute('value', slugify(titleInput.value));
});
