
<template>


  <div id="bg-container" class="position-relative top-0">
    <div id="bg-cover" class="position-absolute w-100 h-100" :style="{backgroundImage: currentTrack ? `url(${currentTrack.albumCover})` : 'none'}"></div>

    <div class="position-absolute end-0 input-group input-group-sm w-25 float-end m-lg-3 mix-blend" style="min-width: 500px;">
      <input class="form-control form-control-sm transparent-input" v-model="url" placeholder="유튜브 링크"/>
      <!-- <button class="btn btn-sm btn-outline-light" @click="downloadVideo"> -->
      <button class="btn btn-sm btn-outline-light" @click="searchYT">
        <Youtube class="text-danger" />
      </button>
    </div>

    <div class="d-flex row align-items-center justify-content-center" style="height: 100vh;">
      <img id="currentCover" class="col-lg-6 shadow-lg rounded-4 z-1 h-auto" v-if="currentTrack" :src="currentTrack.albumCover" :alt="currentTrack.track" />
      <div v-else class="rounded-2" align="center">
        <base-svg-type-path viewBox="0 0 24 24" width="256" height="256" iconColor="var(--bs-secondary)">
        <music-slash/>
        </base-svg-type-path>
      </div>
      <div v-if="currentTrack" class="col-lg-6 mb-5 me-3 me-lg-0 mb-lg-0 ms-3 text-white">
        <h3>
          <strong class="mix-blend">{{ track }}</strong>
        </h3>
        <h5>
          <small class="mix-blend">{{ artist }}</small>
        </h5>
        <h5>
          <small class="mix-blend">{{ album }}</small>
        </h5>
      </div>
    </div>
  </div>

  <!-- 하단 바 -->
  <div class="navbar bg-dark navbar-dark fixed-bottom py-0 row" style="box-shadow: 0 0 10px rgba(0,0,0,.5) !important; ">
    
    <!-- 재생 바 -->
    <div id="current" class="progress w-100 rounded-0" style="height:6px">
      <div class="progress-bar bg-primary" style="width:70%"></div>
    </div>
    <!-- 재생 바 끝 -->

    <!-- 노래 컨트롤 -->
    <div id="control" class="d-inline-flex py-2 align-items-center">

      <!-- 노래 정보 -->
      <div class="col d-inline-flex me-5">
        <div id="cover" class="d-inline-flex rounded-2">

          <img class="rounded ms-2" width="64" height="64" v-if="currentTrack" :src="currentTrack.albumCover" :alt="currentTrack.track" />

          <div v-else class="rounded-2" >
            <base-svg-type-path viewBox="0 0 24 24" width="64" height="64" iconColor="var(--bs-secondary)">
            <music-slash/>
            </base-svg-type-path>
          </div>
          
          <div class="text-light ms-3">
            <h5 class="ellipsis">
              <strong>{{ track }}</strong>
            </h5>
            <h6 class="ellipsis">
              <small>{{ artist }}</small>
            </h6>
          </div>

        </div>
      </div>
      <!-- 노래 정보 끝 -->

      <!-- 컨트롤 바 -->
      <div class="col d-inline-flex me-5">
        <Shuffle :style="{color : shuffleColor}" class="fs-5 ms-auto me-5" role="button" @click="shuffleTrack" :stroke-width="2.5" />
        
        <font-awesome-icon :icon="['fas', 'backward-step']" class="fs-3 text-light me-5" role="button" @click="prevTrack"/>
        <font-awesome-icon :icon="trackStatus" class="fs-3 text-light me-5" role="button" @click="playTrack"/>
        <font-awesome-icon :icon="['fas', 'forward-step']" class="fs-3 text-light me-5" role="button" @click="nextTrack"/>

        <Repeat v-if="repeat != 1" :style="{color : repeatColor}" class="fs-5 me-auto me-5" role="button" @click="repeatTrack" :stroke-width="2.5" />
        <Repeat1 v-else role="button" :style="{color : repeatColor}" class="fs-5 me-5 me-auto" @click="repeatTrack" :stroke-width="2.5"/>
      </div>
      <!-- 컨트롤 바 끝 -->

      <div class="col d-inline-flex">

        <VolumeOff v-if="mute" :stroke-width="2.5" class="ms-auto me-3 text-light pointer" @click="muteSound"/>
        <Volume2 v-else :stroke-width="2.5" class="ms-auto me-3 text-light pointer"  @click="muteSound"/>
        <input type="range" class="form-range w-25 me-3 d-none d-lg-block" step="10" v-model="volume"  :data-alt="volume">
        <div class="dropup">
          <ListMusic class="text-light fs-5 pointer ms-auto me-5 dropdown-toggle" data-bs-toggle="dropdown" :stroke-width="2.5" />
          <div class="dropdown-menu dropdown-menu-end">
            
          </div>
        </div>
        
      </div>

    </div>
    <!-- 노래 컨트롤 끝 -->

  </div>
</template>
<script setup>

  import { Repeat } from 'lucide-vue-next';
  import { Repeat1 } from 'lucide-vue-next';
  import { Shuffle } from 'lucide-vue-next';
  import { ListMusic } from 'lucide-vue-next';
  import { Volume2 } from 'lucide-vue-next';
  import { VolumeOff } from 'lucide-vue-next';
  import { Youtube } from 'lucide-vue-next';
  import axios from 'axios';

</script>

<script>
  export default {
    metaInfo :{
      title: 'Default Title',
      titleTemplate: '%s | MusicPlayer'
    },
    data() {
      return {
        playlist : [
          // {
          //   track : 'Without Me',
          //   artist : 'Eminem',
          //   album : 'The Eminem Show',
          //   albumCover : 'https://image.bugsm.co.kr/album/images/500/246/24633.jpg',
          //   audio : ''
          // },
          // {
          //   track : 'Viva la Vida',
          //   artist : 'Coldplay',
          //   album : 'Viva la Vida or Death and All His Friends',
          //   albumCover : 'https://i.namu.wiki/i/Oa3FTKskSyIy6rbnerWoR1vM-Ar_t4PwHGVgqaRD34bjJlIO7L-zwQuUsm-D4J45AQ-JooKJ_UFXlmyYvJAx6Q.webp',
          //   audio : ''
          // },
          // {
          //   track : 'Stan',
          //   artist : 'Eminem',
          //   album : 'The Marshall Mathers LP',
          //   albumCover : 'https://i.scdn.co/image/ab67616d0000b273dbb3dd82da45b7d7f31b1b42',
          //   audio : ''
          // }
        ],
        currentIndex : 0, // 현재 재생중인 노래의 인덱스 값
        play : true, // 재생중?
        repeat : -1, // 반복 재생?  -1 > false / 0 > 전체 반복 / 1 > 한 곡 반복
        shuffle : false, // 랜덤 재생?  false > 정상 재생 / true > 무작위 재생
        repeatColor : 'var(--bs-light)',
        shuffleColor : 'var(--bs-light)',
        mute : false,
        volume: 50,  // 초기 볼륨 값
        prevVolume: 50,  // 음소거 이전 볼륨 값
        searchInput: 'd-none'
      }
    },
    computed : {
      currentTrack() {
        return this.playlist.length ? this.playlist[this.currentIndex] : ''; // 인덱스 값을 받아오게 설정함
      },
      track() {
        return this.currentTrack?.track || '재생 중인 곡 없음';
      },
      artist(){
        return this.currentTrack?.artist || '알 수 없는 아티스트';
      },
      album(){
        return this.currentTrack?.album || '알 수 없는 앨범';
      },
      trackStatus() {
        return this.play ? ['fas', 'pause'] : ['fas', 'play'];
      },
    },
    methods : {
      nextTrack() {

        if (this.currentIndex < this.playlist.length - 1) 
        {
          this.currentIndex++;
        } 
        else 
        {
          this.currentIndex = 0; // 인덱스의 마지막이면 인덱스를 처음으로 돌림
        }

      },
      prevTrack() {

        if (this.currentIndex > 0) 
        {
          this.currentIndex--;
        } 
        else 
        {
          this.currentIndex = this.playlist.length - 1; // 인덱스의 처음이면 인덱스를 마지막으로 돌림
        }

      },
      repeatTrack() {

        // if (this.repeatTrack == -1) {
        //   this.repeatColor = 'var(--bs-dark)'; // 반복 재생 없음이면 다음 색깔 검정
        //   this.repeatTrack++; // repeatTrack에 1을 더해줌
        // }
        // else if (this.repeatTrack == 0) {
        //   this.repeatColor = 'var(--vs-dark)'; // 반복 재생이면 다음 색은 바꾸지 않음 ( 디버그용 입력 )
        //   // 아이콘도 바꿔야함
        //   this.repeatTrack++; // 위와 동일
        // }
        // else if (this.repeatTrack == 1) {
        //   this.repeatColor = 'var(--vs-secondary)'; // 한곡 반복이면 처음 색(--bs-secondary)로 바꿔줌
        //   // 아이콘도 바꿔야함
        //   this.repeatTrack = -1; // 한곡 반복이면 repeatTrack을 -1로 교체해줌
        // }
        
        this.repeat = (this.repeat + 1) % 3;

        switch (this.repeat) {
          case 0 :
            this.repeatColor = 'var(--bs-primary)'
            break;
          case 1 :
            this.repeatColor = 'var(--bs-primary)'
            break;
          default :
            this.repeatColor = 'var(--bs-light)'
        }

      },
      shuffleTrack() {

        this.shuffle = !this.shuffle; // 상태값 반대로 변경
        this.shuffleColor = this.shuffle ? 'var(--bs-primary)' : 'var(--bs-light)';

      },
      playTrack() {
        this.play = !this.play; // 플레이 버튼 누르면 true false 반대로 바꾸기
      },
      muteSound() {
        
        // 음소거 버튼 클릭시 원래 값은 저장해둬야함
        if (this.mute) {
          // 원래 볼륨값 가져오기
          this.volume = this.prevVolume;
        }
        else
        {
          // 지금 볼륨값을 저장해두고, 실제 볼륨을 0으로 변경
          this.prevVolume = this.volume;
          this.volume = 0
        }

        this.mute = !this.mute // 음소거 버튼 누르면 boolean 변경

      },
      searchVisible() {
        this.searchInput = !this.searchInput
      },
      async downloadVideo() {
        if (!this.url) {
          this.message = "Please enter a URL.";
          return;
        }
        try {
          const response = await axios.post("http://localhost:5000/download", {
            url: this.url,
          });
          
          if (response.data.playlist) {

            this.playlist.push(response.data.playlist);

          }

        } catch (error) {
          this.message = error.response?.data?.error || "An error occurred.";
        }
      },
      create(){
        console.log(process.env)
      },
      searchYT(){

        const params = {
          key:process.env.VUE_APP_YOUTUBE_DATA_API_KEY,
          q: this.url,
          part: "snippet",
          type: "video",
          maxResults: 5,
          fields: "items(id,snippet(title,thumbnails),contentDetails.duration)",
          videoEmbeddable: true,
        };

        const Data = axios.get("https://www.googleapis.com/youtube/v3/search", { params })

        return Data;
      }
    }
  }
</script>

<style>
  body {background-color: var(--bs-secondary-color) !important; height: 100vh;}
  #nowPlay{min-width:400px;}
  .pointer {cursor: pointer;}
  .ellipsis {
    overflow: hidden; 
    white-space: nowrap; 
    text-overflow: ellipsis; 
    max-width: 10vw;
  }

  #bg-container {
    width: 100vw;
    height: 100vh;
    overflow: hidden;
  }
  
  #bg-cover {
    left: 0;
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    filter: blur(8px);
    z-index: -1;
  }
  
  #currentCover {
    width: 300px;
    height: 300px;
    background-size: cover;
    background-position: center;
  }

  .mix-blend{
    mix-blend-mode: difference;
  }
  input.transparent-input{
    background-color:transparent !important;
    color:var(--bs-light) !important;
  }
  input.transparent-input::placeholder{
     color: var(--bs-light) !important;
  }
</style>
