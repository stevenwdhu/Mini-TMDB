const toggleHearthBtn = (btn) => {
  if (btn.children[1].classList.contains("d-block")) {
    btn.children[1].classList.replace("d-block", "d-none");
    btn.children[0].classList.replace("d-none", "d-block");
  } else {
    btn.children[0].classList.replace("d-block", "d-none");
    btn.children[1].classList.replace("d-none", "d-block");
  }
};

let movieIdList =
  localStorage
    .getItem("movieList")
    ?.split(",")
    .filter((v) => v) || [];
let tvIdList =
  localStorage
    .getItem("tvList")
    ?.split(",")
    .filter((v) => v) || [];

[movieIdList, tvIdList].forEach((list) => {
  list.forEach((id) => {
    const btn = document
      .querySelector(`[media-id='${id}']`)
      ?.querySelector(".favourite-btn");
    btn && toggleHearthBtn(btn);
  });
});
document.querySelector("#navFavourite").href =
  `/favourite?movie=${movieIdList}&tv=${tvIdList}`;

document.querySelectorAll(".media-card").forEach((card) => {
  const btn = card.querySelector(".favourite-btn");
  const mediaId = card.getAttribute("media-id");
  const mediaType = card.getAttribute("media-type");
  btn.addEventListener("click", (ev) => {
    ev.preventDefault();
    toggleHearthBtn(btn);
    switch (mediaType) {
      case "movie":
        if (movieIdList.includes(mediaId)) {
          movieIdList = movieIdList.filter((id) => id !== mediaId);
        } else {
          movieIdList.push(mediaId);
        }
        localStorage.setItem("movieList", movieIdList);
        break;
      case "tv":
        if (tvIdList.includes(mediaId)) {
          tvIdList = tvIdList.filter((id) => id !== mediaId);
        } else {
          tvIdList.push(mediaId);
        }
        localStorage.setItem("tvList", tvIdList);
        break;
    }
    document.querySelector("#navFavourite").href =
      `/favourite?movie=${movieIdList}&tv=${tvIdList}`;
  });
});
