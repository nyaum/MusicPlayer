
<template>
  <div class="container vh-100 w-100">
    <div class="row align-items-center h-100">
      <div class="col-10 mx-auto">
          <div class="jumbotron">
            <div id="nowPlay" class="card container-fluid p-0 w-50">
              
              <div class="card-header border-0">
                <font-awesome-icon :icon="['fas', 'bars']" class="float-end text-secondary fs-5 pointer" />
              </div>

              <div class="card-body p-4">

                <div id="cover" class="p-1 rounded-2 text-center border d-flex justify-content-center align-items-center">

                  <img class="rounded w-100 d-block" v-if="currentTrack" height="450" :src="currentTrack.albumCover" :alt="currentTrack.track" />

                  <!--https://image.bugsm.co.kr/album/images/500/246/24633.jpg-->

                  <div v-else class="rounded-2 flex-grow-1" >
                    <base-svg-type-path viewBox="0 0 24 24" width="100" height="100" iconColor="var(--bs-secondary)" icon-name="music-slash">
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

                <div id="control" class="row my-5 text-center align-items-center">

                  <div class="col">
                    <font-awesome-icon :icon="['fas', 'shuffle']" class="text-secondary fs-5" role="button" />
                  </div>

                  <div class="col">
                    <font-awesome-icon :icon="['fas', 'backward-step']" class="fs-1" role="button" @click="prevTrack"/>
                  </div>
                  <div class="col">
                    <font-awesome-icon :icon="['fas', 'play']" class="fs-1" role="button"/>
                  </div>
                  <div class="col">
                    <font-awesome-icon :icon="['fas', 'forward-step']" class="fs-1" role="button" @click="nextTrack"/>
                  </div>

                  <div class="col">
                    <font-awesome-icon :icon="['fas', 'repeat']" class="text-secondary fs-5" role="button"/>
                  </div>

                </div>

                <div id="current" class="progress">
                  <div class="progress-bar bg-dark" style="width:70%"></div>
                </div>

              </div>
            </div>
          </div>  
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        playlist : [
          {
            track : 'Without me',
            artist : 'Eminem',
            albumCover : 'https://image.bugsm.co.kr/album/images/500/246/24633.jpg'
          },
          {
            track : 'Viva la Vida',
            artist : 'Coldplay',
            albumCover : 'https://i.namu.wiki/i/Oa3FTKskSyIy6rbnerWoR1vM-Ar_t4PwHGVgqaRD34bjJlIO7L-zwQuUsm-D4J45AQ-JooKJ_UFXlmyYvJAx6Q.webp'
          },
          {
            track : 'Stan',
            artist : 'Eminem',
            albumCover : 'https://i.scdn.co/image/ab67616d0000b273dbb3dd82da45b7d7f31b1b42'
          }
        ],
        currentIndex : 0, // 현재 재생중인 노래의 인덱스 값
        repeat : -1, // 반복 재생?  -1 > false / 0 > 전체 반복 / 1 > 한 곡 반복
        shuffle : false // 랜덤 재생?  false > 정상 재생 / true > 무작위 재생
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

      }
    }
  }
</script>

<style>
  body {background-color: var(--bs-secondary-color) !important; height: 100vh;}
  #nowPlay{min-width:400px;}
  #cover{min-height: 450px;}
  .pointer {cursor: pointer;}
</style>
