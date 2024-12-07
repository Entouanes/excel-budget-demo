<div class="card bg-base-200 w-1/3 shadow-lg h-full" >
    <div class="card-body ">
        <h1 class="card-title">Select a file to analyse</h1>
        <label class="form-control w-full space-y-3">
            <div class="label">
                <span class="label-text">Supported format(s): .xlsx</span>
            </div>
            <input type="file" class="file-input file-input-bordered w-full" />
            <p>Optionally, provide additional information to guide the generator</p>    
            <textarea class="textarea textarea-bordered h-52" placeholder="Format the outupt as follow..."></textarea>
            <div class="card-actions">
                <button class="btn btn-neutral">SUMMARIZE</button>
            </div>
        </label>
    </div>
</div>
<div class="card bg-base-200 w-2/3 shadow-lg h-full">
    <div class="card-body">
        <h1 class="card-title">File summary</h1>
        <textarea class="textarea" placeholder="No file was provided" disabled={true}></textarea>
    </div>
</div>