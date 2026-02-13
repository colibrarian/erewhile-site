export async function onRequest(context) {
  const request = context.request;
  const url = new URL(request.url);

  
  if (
    url.pathname.startsWith("/assets") ||
    url.pathname.startsWith("/favicon") ||
    url.pathname.startsWith("/robots") ||
    url.pathname.startsWith("/sitemap")
  ) {
    return context.next();
  }

 
  const country = request.cf?.country || "EU";

  let folder = "eu";
  if (country === "AU") folder = "au";
  else if (country === "US") folder = "us";

  
  if (
    url.pathname.startsWith("/eu") ||
    url.pathname.startsWith("/au") ||
    url.pathname.startsWith("/us")
  ) {
    return context.next();
  }

  
  if (url.pathname === "/") {
    url.pathname = `/${folder}/index.html`;
  } else {
    url.pathname = `/${folder}${url.pathname}`;
  }

  return context.rewrite(url);
}
