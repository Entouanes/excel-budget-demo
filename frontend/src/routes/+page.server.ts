import type { Actions } from './$types';

export const actions = {
	default: async ( {request} ) => {
		// eslint-disable-next-line @typescript-eslint/no-unused-vars
		const formData = await request.formData();
        
        const response = await fetch('http://localhost:8000/summarize/', {
            method: 'POST',
            body: formData
        });

        if (response.ok) {
            return { success: true };
        } else {
            return { success: false };
        }
	},
} satisfies Actions;