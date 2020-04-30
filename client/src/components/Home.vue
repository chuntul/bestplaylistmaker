<template>
  <div class="home">
    <h1>BestPlaylistMaker(BPM)</h1>
    <h2>
      A website that allows you to create playlists of songs
      you like, within a certain bpm range.
    </h2>
    <h3>
      ( Is it really the best playlist maker? Probably not. I did it for the name though. )
    </h3>
    <button v-on:click="login">Login</button>
  </div>
</template>

<script>
export default {
  name: 'Home',
  methods: {
    login() {
      window.location.replace('/login');
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.home {
  background:#ddfacf;
  height:100vh;
  display:flex;
  flex-direction:column;
  justify-content: center;
  align-items:center;
}
.home > * {
  margin:30px 0px;
}
</style>
