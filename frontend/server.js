var getPixels = require("get-pixels")

getPixels("http://images.nationalgeographic.com/wpf/media-live/photos/000/762/cache/panda-trees-woods-990-dl_76256_160x120.jpg", function(err, pixels) {
  if(err) {
    console.log("Bad image path")
    return
  }
  console.log("got pixels", pixels.data.get(0))
})
