<script lang="ts">
	import '../app.css';
	let { children } = $props();
</script>

<div class="navbar bg-base-200 px-10 shadow-md h-20">
	<div class="navbar-start">
		<h1 class="text-xl font-bold">SummaRise</h1>
	</div>
	<div class="navbar-end">
		<a href="/" class="btn btn-outline">Settings</a>
	</div>
</div>
<div class="container w-2/3 mx-auto my-[5rem] justify-around gap-[3rem] flex">
	{@render children()}
</div>
