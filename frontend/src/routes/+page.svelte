<script lang="ts">
    import { enhance } from "$app/forms";
    let summary : string | undefined | void = $state(undefined);
    let loading = $state(false)

    const fetchSummary: any = () => {
        loading = true;

        return async ( { update }: { update: (data: { summary: string | undefined | void}) => Promise<void> } ) => {
            loading = false;
            summary = await update({ summary });
            console.log(summary)
        }
    }
</script>

<div class="card bg-base-200 w-1/3 shadow-lg h-full" >
    <div class="card-body ">
        <h1 class="card-title">Select a file to analyse</h1>
        <form method="POST" enctype="multipart/form-data" use:enhance={fetchSummary}>
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
                    placeholder="Format the outupt as follow..." 
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
            <textarea class="textarea" placeholder="No file was provided" disabled={summary==null}></textarea>
        {:else}
            <div class="skeleton h-52 w-full"></div>
        {/if}
    </div>
</div>