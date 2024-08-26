<script>
  import { onMount } from "svelte";
  import { writable } from "svelte/store";
  import { backendUrl } from "../../config.js";

  export let address = "";

  const balance = writable(null);

  const fetchBalance = async () => {
    if (!address) {
      return;
    }
    const response = await fetch(`${backendUrl}balances/${address}`);
    const data = await response.json();
    balance.set(data.balance.toString());
  };

  onMount(() => {
    fetchBalance();
  });
</script>

<svelte:head>
  <title>Wallet balance</title>
  <meta name="description" content="Balances" />
</svelte:head>

<div class="text-column">
  <h1>Wallet balance</h1>
  <div class="input-group">
    <input
      type="text"
      bind:value={address}
      placeholder="Enter Wallet Address"
    />
    <button on:click={fetchBalance}>Get Balance</button>
  </div>
  <p>
    Balance: {#if $balance}
      {$balance}
    {/if}
  </p>
</div>

<style>
  .text-column {
    max-width: 600px;
    margin: 0 auto;
    padding: 20px;
    font-family: Arial, sans-serif;
  }

  .input-group {
    display: flex;
    gap: 10px;
  }

  input[type="text"] {
    flex: 1;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 16px;
  }

  button {
    padding: 10px 20px;
    border: none;
    border-radius: 4px;
    background-color: white;
    font-size: 16px;
    cursor: pointer;
    border: 1px solid #ccc;
  }

  button:hover {
    background-color: grey;
  }

  p {
    font-size: 18px;
    margin-top: 20px;
    padding: 10px;
    display: inline-block;
    text-align: center;
  }
</style>
