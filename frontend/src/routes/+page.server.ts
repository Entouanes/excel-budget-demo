import type { Actions } from './$types';

export const actions = {
	default: async ( {request} ) => {
		// eslint-disable-next-line @typescript-eslint/no-unused-vars
		const formData = await request.formData();
        
        const response = await fetch('http://localhost:8000/summarize/', {
            method: 'POST',
            body: formData
        });
        
        // Sleep 1 second to simulate a long running task
        await new Promise(resolve => setTimeout(resolve, 2000));

        if (response.ok) {
            const data = await response.json();
            return { success: true, data };
        } else {
            const error = await response.json();
            return { success: false, error };
        }
	},
} satisfies Actions;