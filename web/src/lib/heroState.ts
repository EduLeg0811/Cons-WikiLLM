// Flag de módulo: vira true na 1ª busca e nunca volta a false enquanto o SPA
// estiver carregado. Compartilhado entre Consulta e Editor sem precisar de
// contexto React.
let _searched = false;

export function markSearched() {
  _searched = true;
}

export function hasEverSearched() {
  return _searched;
}
