<template>
    <h1 class="funny-title section-title" >Fetrisa Toy</h1>
    <div class="container">
        <table  id="maket">
            <tr>
                <td id="leftcol"><SidebarMenu/></td>
                <td id="rightcol"><b-icon class="h1 mb-2" icon="search" aria-hidden="true"></b-icon></td>
                <td id="rightcol"><b-icon class="h1 mb-2" icon="person-fill" aria-hidden="true"></b-icon></td>
                <td id="rightcol"><b-icon class="h1 mb-2" icon="basket3-fill" aria-hidden="true"></b-icon></td>
                <td id="rightcol"><b-icon class="h1 mb-2" icon="suit-heart-fill" aria-hidden="true"></b-icon></td>
            </tr>
        </table>
        <br>
        <br>
        <TabContent/>
    </div>
      <router-view/>
</template>
<script>
import TabContent from "./components/Base.vue"
import SidebarMenu from "@/components/Sidebar.vue";
export default {
    name: 'App',
    components: {
        SidebarMenu,
        TabContent,

    }
}
</script>

<style>
#maket {
    width: 100%; /* Ширина всей таблицы */
   }
   TD {
    vertical-align: top; /* Вертикальное выравнивание в ячейках */
    padding: 5px; /* Поля вокруг ячеек */
   }
   TD#leftcol {
    width: 200px; /* Ширина левой колонки */
   }
   TD#rightcol {
   }

@import "https://fonts.googleapis.com/css?family=Russo+One";

h1.funny-title {
    border-top: 5px solid #d3b7c8;
    border-bottom: 5px solid #d3b7c8;
    font-size: 70px;
    text-align: center;
    margin-top: 40px;
    margin-bottom: 5px;
    text-transform: capitalize;
    font-family: cursive;
    font-weight: 900;
    letter-spacing: 8px
}

@-webkit-keyframes move-background {
    0% {
        background-position: -300px 0
    }
    100% {
        background-position: 300px -300px
    }
}

@-moz-keyframes move-background {
    0% {
        background-position: -300px 0
    }
    100% {
        background-position: 300px -300px
    }
}

@keyframes move-background {
    0% {
        background-position: -300px 0
    }
    100% {
        background-position: 300px -300px
    }
}

.section-title {
    -webkit-animation-play-state: running;
    -moz-animation-play-state: running;
    animation-play-state: running;
    color: transparent;
    background: url(https://obninsksite.ru/assets/theme/images/blog/square.svg) no-repeat #d3b7c8;
    background-size: cover;
    -webkit-text-fill-color: transparent;
    -moz-text-fill-color: transparent;
    -webkit-background-clip: text;
    -moz-background-clip: text;
    background-clip: text;
    -webkit-animation: move-background 20s infinite linear alternate;
    -moz-animation: move-background 20s infinite linear alternate;
    animation: move-background 20s infinite linear alternate
}

.container {
    margin-top: 5%;
    margin-right: 50%;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
