interface SiteConfig {
	author: string
	title: string
	description: string
	lang: string
	ogLocale: string
	shareMessage: string
	paginationSize: number
}

export const siteConfig: SiteConfig = {
	author: 'Mikah Yobrats', // Site author
	title: 'Error Bitz', // Site title.
	description: 'Tech Blog with error solving capabilities', // Description to display in the meta tags
	lang: 'en-GB',
	ogLocale: 'en_GB',
	shareMessage: 'Share this error fix', // Message to share a post on social media
	paginationSize: 10 // Number of posts per page
}
