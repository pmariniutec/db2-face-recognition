<template>
	<v-container>
		<h3 class="headline">
			Face recognition using K nearest neighbor
		</h3>
		<QueryImageUpload />
	</v-container>
</template>

<script>
import QueryImageUpload from '@/components/QueryImageUpload.vue'

export default {
	name: 'Home',
	components: {
		QueryImageUpload
	}
}
</script>
