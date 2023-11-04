<script>
  import { io } from 'socket.io-client'

  $: lightup = Array(64).fill(false);

  const socket = io();

  socket.on("ping", (arg) => {
    console.log(arg, typeof arg);

    let index = arg - 1;

    lightup[index] = true;

    const myTimeout = setTimeout((i) => {
      lightup[i] = false;
    }, 500, index);
  });

  async function sendIt() {
    const response = await fetch("/ls/ping");
  }

</script>

<div class="container">
  <div class="title">
    <h1>
      👨🏻Long Stache👨🏻
    </h1>
  </div>
  <div class="control-row">
    <button on:click={() => {sendIt()}}>Send It</button>
  </div>
  <div class="board">
    {#each lightup as value, i}
      <div class="board__light" class:board__light--lit={value}></div>
    {/each}
  </div>
</div>

<style lang="sass">
  .title
    display: flex
    justify-content: center

    h1
      margin: 0

  button
    background-color: white
    color: black
    border-radius: 10em
    font-size: 17px
    font-weight: 600
    padding: 1em 2em
    cursor: pointer
    transition: all 0.3s ease-in-out
    border: 1px solid black
    box-shadow: 0 0 0 0 black

    &:hover 
      transform: translateY(-4px) translateX(-2px)
      box-shadow: 2px 5px 0 0 black

    &:active 
      transform: translateY(2px) translateX(1px)
      box-shadow: 0 0 0 0 black

  .container
    margin: 0 auto
    gap: 10px
    display: flex
    flex-flow: column

  .board
    display: grid
    gap: 10px
    grid-template-columns: 50px 50px 50px 50px 50px 50px 50px 50px

    &__light
      background-color: black
      height: 50px
      width: 50px
      transition: background-color 1000ms linear

      &--lit
        background-color: #DDD
        transition: background-color 100ms linear
</style>
