<script>
  import { onMount } from "svelte";
  import { backendUrl } from "../config.js";

  let greeting = "Loading...";

  onMount(async () => {
    console.log("Fetching data from server...");
    console.log("Backend URL:", backendUrl);
    try {
      const response = await fetch(backendUrl);
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      const data = await response.text();
      console.log("Response data:", data);
      greeting = data;
    } catch (error) {
      greeting = `Error: ${error.message}`;
      console.log("Fetch error:", error);
    }
  });
</script>

<h1>{greeting}</h1>
