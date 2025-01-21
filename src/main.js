import { createApp } from 'vue'
import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { fas } from '@fortawesome/free-solid-svg-icons'
import { far } from '@fortawesome/free-regular-svg-icons'
import { fab } from '@fortawesome/free-brands-svg-icons'

import App from './App.vue'

// BootStrap 5.3.3v
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'

import BaseSvgTypePath from './components/svg/base/BaseSvgTypePath.vue'
import SvgMusicSlash from './components/svg/svgs/SvgMusicSlash.vue'

// import SvgRepeat from './components/svg/svgs/SvgRepeat.vue'
// import SvgRepeatOne from './components/svg/svgs/SvgRepeatOne.vue'
// import SvgShuffle from './components/svg/svgs/SvgShuffle.vue'



const app = createApp(App)

library.add(
    fas,
    far,
    fab
)
app.component('font-awesome-icon', FontAwesomeIcon)
app.component('base-svg-type-path', BaseSvgTypePath)
app.component('music-slash', SvgMusicSlash)
// app.component('repeat-track', SvgRepeat)
// app.component('repeat-one-track', SvgRepeatOne)
// app.component('shuffle-track', SvgShuffle)
app.mount("#app")

//createApp(App).mount('#app')
