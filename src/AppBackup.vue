
<template>
  <div class="container vh-100 w-100">
    <div class="row align-items-center h-100">
      <div class="col-lg-10 mx-auto">
          <div class="jumbotron">
            
            <!-- 뮤직 플레이어 -->
            <div id="nowPlay" class="card container-fluid p-0 w-50">
              
              <div class="card-header border-0 d-flex">
                <Search class="text-secondary fs-5 pointer me-auto" :stroke-width="2.5" @click="searchVisible" />
                <ListMusic class="text-secondary fs-5 pointer ms-auto" :stroke-width="2.5" />
              </div>

              <div class="card-body p-4">

                <!-- 곡 정보 -->
                <div id="cover" class="p-1 rounded-2 text-center border d-flex justify-content-center align-items-center">

                  <img class="rounded w-100 d-block" v-if="currentTrack" :src="currentTrack.albumCover" :alt="currentTrack.track" />

                  <div v-else class="rounded-2" >
                    <base-svg-type-path viewBox="0 0 24 24" width="100" height="100" iconColor="var(--bs-secondary)" style="min-height: 450px;">
                    <music-slash/>
                    </base-svg-type-path>
                  </div>
                  
                </div>
                
                <hr>

                <h5>
                  <strong>{{ track }}</strong>
                </h5>
                
                <span>
                  <small class="text-secondary">{{ artist }}</small>
                </span>
                <!-- 곡 정보 끝 -->

                <!-- 재생 바 -->
                <div id="current" class="progress mt-3">
                  <div class="progress-bar bg-dark" style="width:70%"></div>
                </div>
                <!-- 재생 바 끝 -->

                <!-- 노래 컨트롤 -->
                <div id="control" class="row my-4 text-center align-items-center">

                  <div class="col">
                    <Shuffle :style="{color : shuffleColor}" class="fs-5" role="button" @click="shuffleTrack" :stroke-width="2.5" />
                  </div>

                  <div class="col">
                    <font-awesome-icon :icon="['fas', 'backward-step']" class="fs-1" role="button" @click="prevTrack"/>
                  </div>
                  <div class="col">
                    <font-awesome-icon :icon="trackStatus" class="fs-1" role="button" @click="playTrack"/>
                  </div>
                  <div class="col">
                    <font-awesome-icon :icon="['fas', 'forward-step']" class="fs-1" role="button" @click="nextTrack"/>
                  </div>

                  <div class="col">
                    <Repeat v-if="repeat != 1" :style="{color : repeatColor}" class="fs-5" role="button" @click="repeatTrack" :stroke-width="2.5" />
                    <Repeat1 v-else role="button" @click="repeatTrack" :stroke-width="2.5" />
                  </div>

                </div>
                <!-- 노래 컨트롤 끝 -->

                <!-- 볼륨 조절 -->
                <div class="d-flex align-items-center">
                  <VolumeOff v-if="mute" :stroke-width="2.5" class="flex-grow-0 me-3 text-dark pointer" @click="muteSound"/>
                  <Volume2 v-else :stroke-width="2.5" class="flex-grow-0 me-3 text-dark pointer"  @click="muteSound"/>
                  <div class="flex-grow-1">
                    <input type="range" class="form-range" step="10" v-model="volume"  :data-alt="volume">
                  </div>
                </div>
                <!-- 볼륨 조절 끝 -->

              </div>
            </div>
          </div>  
      </div>
    </div>
  </div>
</template>

<script setup>

  import { Repeat } from 'lucide-vue-next';
  import { Repeat1 } from 'lucide-vue-next';
  import { Shuffle } from 'lucide-vue-next';
  import { ListMusic } from 'lucide-vue-next';
  import { Volume2 } from 'lucide-vue-next';
  import { VolumeOff } from 'lucide-vue-next';
  import { Search } from 'lucide-vue-next';

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
          {
            track : 'Without me',
            artist : 'Eminem',
            albumCover : 'https://image.bugsm.co.kr/album/images/500/246/24633.jpg',
            audio : ''
          },
          {
            track : 'Viva la Vida',
            artist : 'Coldplay',
            albumCover : 'https://i.namu.wiki/i/Oa3FTKskSyIy6rbnerWoR1vM-Ar_t4PwHGVgqaRD34bjJlIO7L-zwQuUsm-D4J45AQ-JooKJ_UFXlmyYvJAx6Q.webp',
            audio : ''
          },
          {
            track : 'Stan',
            artist : 'Eminem',
            albumCover : 'https://i.scdn.co/image/ab67616d0000b273dbb3dd82da45b7d7f31b1b42',
            audio : ''
          }
        ],
        currentIndex : 0, // 현재 재생중인 노래의 인덱스 값
        play : false, // 재생중?
        repeat : -1, // 반복 재생?  -1 > false / 0 > 전체 반복 / 1 > 한 곡 반복
        shuffle : false, // 랜덤 재생?  false > 정상 재생 / true > 무작위 재생
        repeatColor : 'var(--bs-secondary)',
        shuffleColor : 'var(--bs-secondary)',
        mute : false,
        volume: 50,  // 초기 볼륨 값
        prevVolume: 50,  // 음소거 이전 볼륨 값
        searchInput: 'd-none'
      }
    },
    computed : {
      currentTrack() {
        return this.playlist.length ? this.playlist[this.currentIndex] : null; // 인덱스 값을 받아오게 설정함
      },
      track() {
        return this.currentTrack?.track || '재생 중인 곡 없음';
      },
      artist(){
        return this.currentTrack?.artist || '알 수 없는 아티스트';
      },
      trackStatus() {
        return this.play ? ['fas', 'pause'] : ['fas', 'play'];
      }
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
            this.repeatColor = 'var(--bs-dark)'
            break;
          case 1 :
            this.repeatColor = 'var(--bs-dark)'
            break;
          default :
            this.repeatColor = 'var(--bs-secondary)'
        }

      },
      shuffleTrack() {

        this.shuffle = !this.shuffle; // 상태값 반대로 변경
        this.shuffleColor = this.shuffle ? 'var(--bs-dark)' : 'var(--bs-secondary)';

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
      }
    }
  }
</script>

<style>
  body {background-color: var(--bs-secondary-color) !important; height: 100vh;}
  #nowPlay{min-width:400px;}
  .pointer {cursor: pointer;}
</style>
