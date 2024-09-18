<script>
  import { onMount } from "svelte";
  import { writable } from "svelte/store";
  import { backendUrl } from "../config.js";

  export let address = "0x95222290DD7278Aa3Ddd389Cc1E1d165CC4BAfe5";
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
    }
  };

  onMount(() => {
    fetchBalance();
  });
</script>

<div class="page-wrapper">
  <div class="container">
    <h1>Wallet balance</h1>

    <div class="form-group">
      <label for="address">Wallet Address</label>
      <input
        id="address"
        type="text"
        bind:value={address}
        placeholder="Enter Wallet Address"
      />
    </div>

    <div class="form-row">
      <div class="form-group">
        <label for="network">Network</label>
        <select id="network" bind:value={network}>
          {#each networks as net}
            <option value={net}>{net}</option>
          {/each}
        </select>
      </div>

      <button class="balance-btn" on:click={fetchBalance}>Get Balance</button>
    </div>

    {#if $balance}
      <div class="balance-display">
        <span>Balance:</span>
        <span class="balance-value">{$balance} USDT</span>
      </div>
    {/if}
  </div>
</div>

<style>
  /* Page background and center alignment */
  .page-wrapper {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 50vh;
  }

  /* Container design */
  .container {
    background: white;
    padding: 40px;
    border-radius: 12px;
    box-shadow: 0 6px 18px rgba(0, 0, 0, 0.1);
    max-width: 400px;
    width: 100%;
    text-align: center;
  }

  h1 {
    font-size: 24px;
    color: #333;
    margin-bottom: 20px;
  }

  /* Form group style for inputs */
  .form-group {
    display: flex;
    flex-direction: column;
    margin-bottom: 10px;
    text-align: left;
  }

  .form-group label {
    font-size: 14px;
    margin-bottom: 5px;
  }

  input,
  select {
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 6px;
    font-size: 16px;
    width: 100%;
  }

  input:focus,
  select:focus {
    outline: none;
    border-color: #007bff;
  }

  /* Form row to align dropdown and button horizontally */
  .form-row {
    display: flex;
    gap: 10px;
    justify-content: space-between;
  }

  /* Button styles: thinner and different color */
  .balance-btn {
    padding: 20px;
    margin: 20px 0px;
    background-color: #0077ff;
    height: 50px;
    color: white;
    border: none;
    border-radius: 6px;
    font-size: 14px;
    cursor: pointer;
    transition: background-color 0.3s ease;
    flex-shrink: 0;
  }

  .balance-btn:hover {
    background-color: #e68900;
  }

  /* Balance display style */
  .balance-display {
    margin-top: 20px;
    font-size: 18px;
    color: #333;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px 0;
    border-top: 1px solid #eee;
  }

  .balance-value {
    font-weight: bold;
    color: #0077ff;
  }

  @media (max-width: 500px) {
    .form-row {
      flex-direction: column;
      gap: 15px;
    }
  }
</style>
