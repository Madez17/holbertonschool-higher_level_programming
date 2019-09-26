$.get('https://swapi.co/api/films/?format=json', function (data) {
  const dataTitle = data.results;
  for (const i of dataTitle) {
    $('UL#list_movies').append('<li>' + i.title + '</li>');
  }
});
