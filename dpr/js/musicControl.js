let music = document.getElementById('music')
let video = document.getElementsByTagName('video')[0]
video.style.display = 'none'
playStatus = false

music.onclick = function (){
    if (!playStatus){
        playStatus = true
        video.play()
        music.style.animation = '1s zhuan linear infinite'
    }else if(playStatus){
        playStatus = false
        video.pause()
        music.style.animation = ''
    }
}