module.exports = {
	root: true,
	env: {
		node: true
	},
	'extends': [
		'plugin:vue/recommended',
		'@vue/standard'
	],
	rules: {
		'no-console': process.env.NODE_ENV === 'production' ? 'error' : 'off',
		'no-debugger': process.env.NODE_ENV === 'production' ? 'error' : 'off',
		'vue/html-indent': ['error', 'tab', {
			'attribute': 1,
			'closeBracket': 0,
			'ignores': []
		}],

		'no-new': 0,
		'indent': ['error', 'tab'],
		'no-tabs': 0,
		'quotes': [2, 'single'],
		'one-var': [0, 'never']
	},
	parserOptions: {
		parser: 'babel-eslint'
	}
}
