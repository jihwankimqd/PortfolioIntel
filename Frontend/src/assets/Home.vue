<template>
  <div id="app">

    <!-- <div class="container"> -->

      <section id="home">
          <div class="brand_landing">
            <div id="landing">
              <p>JHK</p>
            </div>
          </div>
          <div class="bg"></div> 
      </section>

      <section id="about">
        <div class="svg-wrapper">

          <svg height="40" width="150">
            <rect id="shape" height="40" width="150" />
          </svg>

            <div id="text">
              <a href="about.html">about</a>
            </div> 
        </div>
          
      </section>

      <section id="projects">
        <div class="svg-wrapper">

          <svg height="40" width="150">
            <rect id="shape" height="40" width="150" />
          </svg>

            <div id="text">
              <a href="portfolio.html">chartjs</a>
            </div> 
        </div>         
      </section>

      <section id="projects">
        <div class="svg-wrapper">

          <svg height="40" width="150">
            <rect id="shape" height="40" width="150" />
          </svg>

            <div id="text">
              <a href="dashboard.html">dashboard</a>
            </div> 
        </div>         
      </section>

      <section id="projects">
        <div class="svg-wrapper">

          <svg height="40" width="150">
            <rect id="shape" height="40" width="150" />
          </svg>

            <div id="text">
              <a href="projects.html">projects</a>
            </div> 
        </div>         
      </section>

    <!-- </div> -->

  </div>
</template>

<script>

export default {
  name: 'App',
  components: {
    
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  height: 100vh;
  line-height: 1.6;
  overflow: hidden;
      /* width: 100%;
      height: 100%; */

      /* CSS Smooth Scroll */
      overflow-y: scroll; 
      scroll-behavior: smooth;
      scroll-snap-type: y mandatory;

      /* overflow: hidden; */  
}
    * {
      margin: 0;
      padding: 0;
    }

   .brand_landing {


      font-size:30px;
      font-weight: bolder;
      position: relative;
      /* margin-top: -20%; */
      
    }
    
    .brand_page {
      
      font-size:20px;
      font-weight: bolder;
      position: relative;
    }

    .bg {
      position: absolute;
      top: 0;
      left: 0;
      z-index: -1;
      opacity: 0;
      transition: 1s;
      pointer-events: none;
      width: 100%;
      height: 100%;
      overflow: hidden;
      color: black;
      background: black;
      padding-bottom:5%;
    }

    .brand_landing:hover~.bg {
      opacity: 1;
      background: #e2a9e5;
      background: -moz-linear-gradient(-45deg, #FB7BA2 5%, #90D5EC 100%);
      background: -webkit-linear-gradient(-45deg,  #FB7BA2 5%, #90D5EC 100%);
      background: linear-gradient(135deg,  #FB7BA2 5%, #90D5EC 100%);
      filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#FB7BA2', endColorstr='#90D5EC',GradientType=1 );
    }

    .container {

    }

    .lead {
      font-size: 1.5rem;
    }

    section {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      text-align: center;
      width: 100%;
      height: 100vh;

      /* Scroll Snap */
      scroll-snap-align: center;
    }


    #about p{
      margin-top: -20%;
    }

    #projects p{
      margin-top: -20%;
    }

    #contact p{
      margin-top: -20%;
    }


  .svg-wrapper {
    margin-top: -45px;
    /* position: relative; */
    width: 150px;
    /*make sure to use same height/width as in the html*/
    height: 40px;
    display: inline-block;
    border-radius: 3px;
    margin-left: 5px;
    margin-right: 5px;
  }

  #shape {
    
    stroke-width: 6px;
    fill: transparent;
    /* opacity: 0; */
    stroke-dasharray: 85 400;
    stroke-dashoffset: -220;
    transition: 1s all ease;
  }

  #landing{
    /* background-color: green; */

    /* margin-top: 200px; */
  }

  #text {
    margin-top: -42px;
  }

  #text a {
    color: black;
    text-decoration: none;
    font-weight: 100;
    font-size: 1.1em;
  }

  .svg-wrapper:hover #shape {
    stroke-dasharray: 50 0;
    stroke-width: 3px;
    stroke-dashoffset: 0;
    stroke: black;
  }


</style>
