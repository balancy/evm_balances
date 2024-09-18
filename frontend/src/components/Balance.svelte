<script>
  import { onMount } from "svelte";
  import { writable } from "svelte/store";
  import { backendUrl } from "../config.js";

  export let address = "";
  export let network = "ETH";

  const balance = writable(null);
  const networks = ["ETH", "BSC", "MATIC", "ARB", "OP", "AVAX", "MNT"];

  const fetchBalance = async () => {
    if (!address || !network) {
      return;
    }
    try {
      const response = await fetch(
        `${backendUrl}/balances?address=${address}&network=${network}`,
      );

      if (!response.ok) {
        throw new Error(`Error: ${response.status} ${response.statusText}`);
      }

      const data = await response.json();
      console.log(data);

      if (Array.isArray(data) && data[0]?.balance !== undefined) {
        balance.set(data[0].balance.toString());
      } else {
        throw new Error("Unexpected response format");
      }
    } catch (error) {
      console.error("Failed to fetch balance:", error);
      balance.set("Error fetching balance");
    }
  };

  onMount(() => {
    fetchBalance();
  });
</script>

<div class="text-column">
  <h1>Wallet balance</h1>
  <div class="input-group">
    <input
      type="text"
      bind:value={address}
      placeholder="Enter Wallet Address"
    />
    <select bind:value={network}>
      {#each networks as net}
        <option value={net}>{net}</option>
      {/each}
    </select>
    <button on:click={fetchBalance}>Get Balance</button>
  </div>
  <p>
    Balance: {#if $balance}
      {$balance} usdt
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
