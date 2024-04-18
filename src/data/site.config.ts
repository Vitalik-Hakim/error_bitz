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
	description: 'Error Bitz (Bits).Stay updated on the latest in technology while finding solutions to your code errors. Discover articles, tips and tricks to conquer challenges', // Description to display in the meta tags
	lang: 'en-GB',
	ogLocale: 'en_GB',
	shareMessage: 'Share this useful post', // Message to share a post on social media
	paginationSize: 100 // Number of posts per page
}
