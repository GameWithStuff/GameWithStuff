
const audio = document.querySelector('audio')
const plays = Array.from(document.querySelectorAll('.play'))
const songName = document.querySelector('.songname')
const srcArray = ['Songs/shapeofyou.mp3', 'Songs/thenights.mp3', 'Songs/seashanty.mp3', 'Songs/supershy.mp3', 'Songs/nightdancer.mp3']
let currentSong = 5
let called = false
plays.forEach((play) => {
    play.onclick = () => {
        songName.innerText = play.previousElementSibling.innerText
        if ((play.firstChild.getAttribute('src') === 'IMG/Pause.png') && !called) {
            play.setAttribute('src', 'IMG/Play.png')
            audio.pause()
        }
        else {

            plays.forEach((eachplay) => {
                eachplay.firstChild.setAttribute('src', 'IMG/Play.png')
            })
            play.firstChild.setAttribute('src', 'IMG/Pause.png')
            if (!(audio.getAttribute('src') === `Songs/${play.id}.mp3`)) {
                audio.setAttribute('src', `Songs/${play.id}.mp3`)
                audio.setAttribute('data-playing', `${play.id}`)
            }
            // else {
            audio.play()
            // }
        }
    }
})

audio.onplay = () => {
    document.querySelector(`.${audio.dataset.playing} img`).setAttribute('src', 'IMG/Pause.png')
}
audio.onpause = () => {
    document.querySelector(`.${audio.dataset.playing} img`).setAttribute('src', 'IMG/Play.png')
}

audio.onended = () => {
    currentSong = currentSong === 5 ? 0 : currentSong + 1
    let called = true
    plays[currentSong].onclick()

}
