// Old bookmarks on the original single-page site.
const sections = {
  about: 'biography/', education: 'biography/#education', experience: 'biography/#experience',
  publications: 'biography/#publications', projects: 'biography/#projects',
  skills: 'biography/#skills', awards: 'credentials/#awards'
};
function followOldBookmark() {
  const id = location.hash.slice(1);
  if (Object.hasOwn(sections, id)) location.replace('/' + sections[id]);
}
followOldBookmark();
window.addEventListener('hashchange', followOldBookmark);
