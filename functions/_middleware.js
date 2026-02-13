export async function onRequest(context) {
  const { request, env, next } = context;
  const url = new URL(request.url);
  const path = url.pathname;

  // Пропускаем статику и любые файлы (включая .html)
  if (
    path.startsWith("/assets/") ||
    path.startsWith("/favicon") ||
    path.startsWith("/robots") ||
    path.startsWith("/sitemap") ||
    /\.[a-zA-Z0-9]+$/.test(path) // <-- fast-website.html попадёт сюда
  ) {
    return next();
  }

  // Страну надёжнее брать из заголовка
  const country = request.headers.get("cf-ipcountry") || "EU";

  let folder = "eu";
  if (country === "AU") folder = "au";
  else if (country === "US") folder = "us";

  // Если уже в /eu /au /us — не трогаем
  if (path.startsWith("/eu/") || path.startsWith("/au/") || path.startsWith("/us/")) {
    return next();
  }

  // Переписываем путь
  if (path === "/") {
    url.pathname = `/${folder}/index.html`;
  } else {
    url.pathname = `/${folder}${path}`;
  }

  // ВАЖНО: отдаём статический ассет через ASSETS
  return env.ASSETS.fetch(new Request(url.toString(), request));
}
