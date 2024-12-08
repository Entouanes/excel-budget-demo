<script lang="ts">
    import { enhance } from "$app/forms";

    // Explicitly type your variables
    let summary: string | null = "No file analysed yet.";
    let loading: boolean = false;

    async function handleSubmit({ formData }: { formData: FormData }): Promise<void> {
        loading = true;

        const response = await fetch('http://localhost:8000/summarize/', {
            method: 'POST',
            body: formData
        });

        // Simulate a long-running task
        await new Promise(resolve => setTimeout(resolve, 2000));
        
        if (response.ok) {
            const data = await response.json();
            console.log(data.summary);
            summary = typeof data.summary === 'string' ? data.summary : JSON.stringify(data.summary);
        } else {
            const error = await response.json();
            summary = "An error occurred.";
        }

        loading = false;
    }
</script>

<div class="card bg-base-200 w-1/3 shadow-lg h-full">
    <div class="card-body">
        <h1 class="card-title">Select a file to analyse</h1>
        <form method="POST" enctype="multipart/form-data" use:enhance={handleSubmit}>
            <label class="form-control w-full space-y-3">
                <div class="label">
                    <span class="label-text">Supported format(s): .xlsx</span>
                </div>
                <input 
                    type="file" 
                    id="file" 
                    name="file"
                    class="file-input file-input-bordered w-full" 
                    disabled={loading}
                />
                <p>Optionally, provide additional information to guide the generator</p>    
                <textarea 
                    class="textarea textarea-bordered h-52" 
                    placeholder="Format the output as follow..." 
                    disabled={loading}
                    id="text"
                    name="text"
                ></textarea>
                <div class="card-actions">
                    {#if !loading}
                        <button class="btn btn-neutral" type="submit">SUMMARIZE</button>
                    {:else}
                        <button class="btn btn-neutral" disabled>
                            <span class="loading loading-spinner loading-sm"></span>
                            SUMMARIZE
                        </button>
                    {/if}
                </div>
            </label>
        </form>
    </div>
</div>

<div class="card bg-base-200 w-2/3 shadow-lg h-full">
    <div class="card-body space-y-3">
        <h1 class="card-title">File summary</h1>
        {#if !loading}
            <div 
                class="rounded-md p-5 bg-base-100 w-full" 
            >
                {summary}
            </div>
        {:else}
            <div class="skeleton h-52 w-full"></div>
        {/if}
    </div>
</div>
