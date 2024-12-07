<script lang="ts">
	import '../app.css';
	let { children } = $props();
</script>

<div class="navbar bg-base-200 p-3 shadow-lg">
	<div class="navbar-start">
		<h1>SummaRise</h1>
	</div>
	<div class="navbar-end">
		<a href="/about" class="btn btn-ghost">About</a>
	</div>
</div>
<div class="container mx-auto flex justify-center gap-10 h-[650px]">
	{@render children()}
</div>
