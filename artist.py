#!/usr/bin/python
import scrapy
import sys
import time
import codecs

from scrapy.selector import Selector
from w3lib.html import remove_tags

class MediumSpider(scrapy.Spider):
	name="medium.com"
	allowed_domains = ['medium.com']
	start_urls = ["https://medium.com/@nathanhubbard/adele-is-the-largest-selling-artist-on-earth-so-what-s-she-going-to-do-about-it-c4014f6643bd?source=false---------1","https://medium.com/@noahbradley/how-i-became-an-artist-4390c6b6656c?source=false---------2","https://medium.com/@SaraJBenincasa/real-artists-have-day-jobs-d99ad0026876?source=false---------3","https://medium.com/great-writers-under-the-sea/artist-vs-businessman-5f998f40180e?source=false---------4","https://medium.com/your-night-job/how-to-become-a-successful-artist-6679029b072f?source=false---------5","https://medium.com/write-with-impact/this-artist-hits-publish-without-asking-for-permission-9d7189741a34?source=false---------6","https://medium.com/evolution-of-the-arts/power-of-artist-and-brand-partnerships-ec11159ceab1?source=false---------7","https://medium.com/@meganvossler/an-open-letter-to-minnesota-artists-8dbfd8ffe9a4?source=false---------8","https://medium.com/@jennwhit/an-artist-s-frustration-a91abf910043?source=false---------9","https://medium.com/@zaksmith_/i-was-talking-to-my-art-dealer-about-artists-i-knew-8a759cf3e577?source=---","https://blog.artlounge.in/artist-showcase-amruta-rokade-mumbai-edda8bdbff04?source=---","https://festivalpeak.com/the-fall-from-artist-to-performer-lady-gaga-s-painful-wake-up-call-3a3940fd7cc2?source=---","https://medium.com/@Amrapali/i-am-raised-and-trained-by-an-award-winning-pioneering-artist-so-early-on-in-life-i-realized-i-am-9286ee15c31b?source=---","https://medium.com/the-mountains-are-calling/outdoor-inspired-artist-spotlight-nicole-gaitan-eb9fe9688af6?source=---","https://medium.com/i-heart-pgh/have-you-seen-me-a-memorial-to-slavery-artist-talk-kickstarter-party-c33d146e16b6?source=---","https://medium.com/@bluebirdartco/artist-feature-peter-foucault-68bc6d2509e8?source=---","https://medium.com/@pixiteapps/artist-interview-oscar-garrigues-5fa0ddf305c?source=---","https://medium.com/@apsysuryodibroto/artistic-skill-does-it-kill-or-does-it-cure-6b1786685e9a?source=---","https://medium.com/movie-time/honoring-modigliani-soutine-in-january-reflecting-on-the-fellowship-of-artists-8c2bb164968?source=---","https://medium.com/@racheltrout/a-painting-that-is-an-act-is-inseparable-from-the-biography-of-the-artist-8125140818bd?source=---","https://medium.com/@joebreaux/still-the-question-is-what-can-big-labels-do-for-artist-who-have-already-created-found-there-niche-205f529a0da4?source=---","https://medium.com/redes-sociales/un-artista-sin-redes-sociales-254ddba13ac8?source=---","https://medium.com/@Bandsintown/bandsintown-trending-artists-and-who-not-to-miss-at-coachella-a9731ece101c?source=---","https://medium.com/@Letkma/thoughts-on-being-an-artist-975dad563396?source=---","https://medium.com/whatevart-section/artist-of-the-month-november-15-385453aaecee?source=---","https://medium.com/@Artisttree/how-to-be-a-successful-artist-7369218ec575?source=---","https://medium.com/@alexhallfilm/get-your-freelance-artist-visa-in-berlin-the-smart-way-e0f5ac2691de?source=---","https://medium.com/2k-stories/gustave-dor%C3%A9-un-artiste-603c1488c10e?source=---","https://medium.com/by-vincent/good-artists-copy-great-artists-steal-58cf294f5f6c?source=---","https://blog.artlounge.in/artist-showcase-vrinda-dugar-jaipur-54c769d54a50?source=---","https://medium.com/@pravanjan.p/every-artist-should-take-this-into-consideration-art-is-priceless-and-the-artist-doing-those-cdcb644a7871?source=---","https://medium.com/@poetandthebench/conversations-with-an-artist-bob-dinetz-f8565c938e2b?source=---","https://medium.com/@rachelkurzyp/do-you-want-to-be-an-artist-9aee559156d4?source=---","https://medium.com/@jlilly/3-key-components-of-every-successful-artist-launch-af026392988a?source=---","https://medium.com/@PoshPublic/artist-spotlight-alesandro-ljubicic-4ff641e13cf7?source=---","https://medium.com/everything-comes/tweets-solitude-forgiveness-artist-35ffe3a22196?source=---","https://medium.com/@adammarx13/artists-live-on-c1d58db80909?source=---","https://medium.com/@isheyelike/jess-is-the-sm-artist-5c2d61410b85?source=---","https://medium.com/@llaguile/artists-f89b0bd3c9f2?source=---","https://medium.com/@bbuzzart/bbuzzart-the-gateway-to-success-for-emerging-artists-480bdd170d64?source=---","https://medium.com/@mriponr/artist-author-web-designer-8dd6d6144f64?source=---","https://medium.com/@markeshellshear/artist-s-connect-with-the-buyer-don-t-hard-sell-4997606d0191?source=---","https://medium.com/@mgebbs/artist-or-entrepreneur-890ea79a1e50?source=---","https://medium.com/@dessyrachms/case-in-to-relief-arts-as-emotionally-embrace-by-sweeping-the-artists-mental-character-4fc8ce2eaded?source=---","https://medium.com/@margie_77089/the-artist-as-entrepreneur-2a3fc909d84f?source=---","https://medium.com/@andimagenheimer/a-portrait-of-the-artist-andi-magenheimer-e8b61d4f9d3a?source=---","https://medium.com/@rickkitagawa/the-single-most-important-quality-of-successful-artists-hint-it-s-not-talent-7e47e08a25d8?source=---","https://medium.com/@RandyAddy/artist-dance-on-a-razors-edge-and-it-can-be-quite-painful-when-cut-e1714d3ea713?source=---","https://medium.com/@catherinearmsden/an-alert-well-hydrated-artist-in-no-acute-distress-episode-five-544a855eccc5?source=---","https://medium.com/@TEDxJohannesburg/michaella-janse-van-vuuren-designer-artist-engineer-1c606e5c44fb?source=---","https://medium.com/voices-of-america/stories-from-a-swing-state-artist-statement-b2e0d661d52b?source=---","https://medium.com/@mariamagenta/maria-magenta-an-artist-who-starts-to-win-people-s-hearts-9a6e2140f497?source=---","https://medium.com/@theCindyLee/an-artist-s-story-the-artist-within-c3a6afee7cee?source=---","https://medium.com/@regus/five-reasons-why-artists-fail-bb7b161fbc58?source=---","https://medium.com/@editformat/artist-neil-ferguson-2760edcc761d?source=---","https://medium.com/@hagnerd/finding-success-as-an-artist-ad6ad9633917?source=---","https://medium.com/@RKZUK/artist-ea09fac2e264?source=---","https://medium.com/ratafire-insights/here-is-an-idea-that-may-change-your-view-on-artist-crowdfunding-b57b0f2c6faa?source=---","https://medium.com/@goodvibepeople/5-ways-goodvibepeople-helps-up-and-coming-artists-ffff60613305?source=---","https://medium.com/@martijnbaudoin/hello-i-am-sivanski-tattoo-artist-f8c10a36b47b?source=---","https://medium.com/@bluebirdartco/artist-feature-tara-gill-e65d19a36bc5?source=---","https://medium.com/@benmcvittie/screw-success-failure-is-what-being-an-artist-is-all-about-2070dd5fdf83?source=---","https://medium.com/@angad/the-artist-d0ab3b0c9aeb?source=---","https://medium.com/@breakzqueen/the-artist-7c7e427c4617?source=---","https://medium.com/@QuotesCosmos/good-artists-copy-great-artists-steal-2c337ac978d7?source=---","https://medium.com/@project_gabe/a-descoberta-do-meu-eu-artista-4b55bda7ffd?source=---","https://medium.com/@lucagiorgio/as-an-artist-the-hardest-part-to-gaining-success-over-social-media-is-promoting-artwork-while-3af489690a64?source=---","https://medium.com/@jefftakaki/starving-artists-gonna-starve-13c45d0c5a8b?source=---","https://medium.com/@elizabethdfoggie/artistmanifesto-d4eb634d537e?source=---","https://medium.com/small-magic/how-to-be-an-artist-7f42f4e0296c?source=---","https://medium.com/@laureltwitchell/amanda-artist-moms-creative-parents-we-have-this-c44ac07b20d5?source=---","https://blog.artlounge.in/5-artists-specializing-in-miniatures-c1ce9fc570ad?source=---","https://medium.com/@Kurt_Rahn/3-things-we-can-learn-from-artist-lorraine-loots-c409fd4aea3a?source=---","https://medium.com/@maestrobilly/os-250-artistas-que-mais-venderam-discos-ever-ad62ab5a1f60?source=---","https://medium.com/@rakhimov.jasur/street-artists-6fe4a6102283?source=---","https://medium.com/@SamanthaBarnes/samantha-barnes-artist-9bae5daa82d?source=---","https://medium.com/@richmathiason/the-daily-prayer-07-27-2015-prayer-for-my-artist-heart-nancy-bowers-rscp-ad7063926b40?source=---","https://medium.com/@TheJessicaMae/why-it-takes-courage-to-be-an-artist-e9439e9d085f?source=---","https://medium.com/@cduffy90/fractured-atlas-articulates-in-fcc-letter-the-importance-of-broadband-to-artists-3f5f65b19d5e?source=---","https://medium.com/@andreahuang/stop-starving-artists-d819b2434426?source=---","https://medium.com/@quaticia/hey-everyone-this-is-quaticia-i-am-a-r-b-and-pop-artist-1a6699e269f9?source=---","https://medium.com/@bbuzzart/call-for-artist-submission-bbuzzshow-shanghai-8d1ea5423dd6?source=---","https://medium.com/@rua_artista/a-rua-e-o-artista-como-se-identificam-6d1b034e0c2?source=---","https://medium.com/@UpstateDiary/vogue-model-artist-christina-kruse-invites-me-into-her-studio-and-home-upstate-n-y-18e24e322c6d?source=---","https://medium.com/@lovevolvecinema/how-to-become-a-known-artist-2a94e94d13d4?source=---","https://medium.com/of-lists/13-travelling-sites-with-10-artist-s-7-mediumish-publications-40a34e68fbe2?source=---","https://medium.com/@anita_morris/every-culture-or-subculture-has-its-cliches-tortured-artist-is-one-of-those-cliches-d6eb6032f75f?source=---","https://medium.com/@imakemeuk/makeup-artistry-that-celebrates-difference-b6d41cad57bd?source=---","https://medium.com/@morrmeroz/what-ratatouille-and-monsters-university-taught-me-about-being-artist-ababb6a30a84?source=---","https://medium.com/@thepainterskeys/serious-artist-ab1aeb440428?source=---","https://medium.com/film-courage/why-do-people-get-mad-when-artists-sell-out-87f76deca83d?source=---","https://medium.com/@BMBRNYC/nyc-artist-brings-disney-females-up-to-date-with-a-modern-twist-799de4bfa8fb?source=---","https://medium.com/@CCCBLab/celluloid-and-self-sufficiency-artist-run-labs-by-elena-duque-1b695b912d67?source=---","https://medium.com/@olyatra/find-so-you-wanna-be-an-artist-podcasts-on-soundcloud-you-d-love-it-19616db7ec00?source=---","https://medium.com/@sbodine120/why-being-a-professional-artist-isn-t-as-bad-as-you-may-think-e0b0fb0996e4?source=---","https://medium.com/@leonieyue/hermitburpcast-09-dear-aspiring-artist-7c86e9fd5fd?source=---","https://medium.com/@parraart/artistmarianic-parra-2016-tree-d%C3%A9clination-drawing-gouache-on-paper-35-35-cm-d8f31cf48c15?source=---","https://medium.com/@photohab/an-interview-with-norwegian-artist-daria-endresen-ffd0a0c745bd?source=---","https://medium.com/@Sundays/the-artist-becomes-bigger-than-the-art-he-or-she-creates-part-1-fce5ee67de69?source=---","https://medium.com/@rishibhattacharya/i-still-am-an-artist-and-will-always-be-one-fc5a1b098695?source=---","https://medium.com/@markeshellshear/this-artist-really-touched-my-heart-i-felt-for-him-been-there-f912f8e75b77?source=---","https://medium.com/@garryzayon/garry-zayon-designer-artist-ef70bc1abcc6?source=---","https://medium.com/@zjonsee/steal-like-an-artist-book-notes-eb2d5fb54e61?source=---","https://medium.com/@dianacapella/artists-protect-your-content-dd04c31f7bce?source=---","https://medium.com/@rohanasmat/artist-s-nature-d65bdce3715d?source=---","https://medium.com/@humblemystery/artist-d44cf29002fc?source=---","https://medium.com/@JarellPerry/an-artist-s-guide-to-grieving-ccd2b59ebf9d?source=---","https://medium.com/@markeshellshear/the-collectors-collection-building-depth-around-an-artist-cbc052b1b2c1?source=---","https://medium.com/@moxiebee/spotlight-on-clay-randle-the-artist-writer-aka-cid-c7942dee86da?source=---","https://medium.com/@cubey_studio/artist-series-jean-michel-basquiat-bcfc8f9dcde5?source=---","https://medium.com/@markeshellshear/artist-if-it-was-easy-every-body-would-be-famous-and-prosperous-b881b2d47652?source=---","https://medium.com/@ninjangge/how-to-not-frustrate-an-artist-a204383e39f?source=---","https://medium.com/@quadrosrelatos/quadros-relatos-depoimento-de-eduardo-faria-97c54c404d24?source=---","https://medium.com/@GingerSnaps/shibby-calling-all-artists-photographers-models-graphic-designers-sketchers-painters-etc-8f3c85d7e6bd?source=---","https://medium.com/@daniellebourg26/artists-why-living-in-new-york-is-still-worth-it-8e1561e61734?source=---","https://medium.com/@Steve_Law/yes-you-re-a-photographer-but-are-you-an-artist-8be9593deb84?source=---","https://medium.com/@mailatkaustubh/lord-help-us-the-artists-are-armed-79655e038530?source=---","https://medium.com/@HilalIsler/i-think-my-dad-might-secretly-be-an-internet-scam-artist-11a84d611b50?source=---","https://medium.com/@noahbradley/21-days-to-be-a-better-artist-48087576f0dd?source=---","https://deardesignstudent.com/two-weeks-notice-is-for-sandwich-artists-e25a78bece1e?source=---","https://medium.com/@castemelijn/are-you-a-scientist-or-an-artist-78ca64b62812?source=---","https://medium.com/human-x-creator/the-artist-you-ve-never-heard-of-who-s-re-awakening-san-francisco-ea3875d49288?source=---","https://medium.com/cuepoint/killing-freemium-is-the-worst-thing-for-artists-5c1b022bad78?source=---","https://medium.com/@genekogan/machine-learning-for-artists-e93d20fdb097?source=---","https://medium.com/art-marketing/what-street-artists-can-teach-us-about-marketing-863b16202c24?source=---","https://medium.com/the-blog-of-james-clear/the-myth-of-creative-inspiration-great-artists-dont-wait-for-motivation-they-do-this-instead-f02841d9a5ce?source=---","https://medium.com/@chrysb/product-designers-artists-of-the-intangible-67798b53835b?source=---","https://medium.com/@kyleTwebster/the-style-problem-for-artists-bb4c79f2582e?source=---","https://medium.com/@pasql/starting-your-career-as-an-artist-on-the-internet-df59601c086a?source=---","https://medium.com/cuepoint/cant-blame-bad-hip-hop-on-white-artists-bdad7765516d?source=---","https://medium.com/@Whatsthehari/artist-or-not-19be97b2328d?source=---","https://medium.com/@davidtrig/the-1-question-every-artist-needs-to-ask-189b8eb77f28?source=---","https://medium.com/@claudiablanton/featured-artist-of-the-week-lisa-marie-from-dawdlingdoodles-16de422a1533?source=---","https://medium.com/@cavendish/what-does-it-mean-to-be-an-artist-118a7aa0cde2?source=---","https://medium.com/@bluebirdletters/crushing-perfectionism-can-slay-artists-or-create-them-b853939dc2a7?source=---","https://medium.com/inexpensive-progress/great-bardfield-artists-90b52079750e?source=---","https://medium.com/self-starter/the-day-i-realized-that-i-wasn-t-an-artist-and-how-it-transformed-my-career-forever-19fecd147fb0?source=---","https://medium.com/cuepoint/why-artist-managers-are-taking-center-stage-4c54f93b1e44?source=---","https://medium.com/cuepoint/kanye-west-does-not-respect-artistry-e583147f4c7d?source=---","https://medium.com/ted-fellows/7-up-and-coming-artists-you-need-to-know-e75594ed5f6a?source=---","https://medium.com/swlh/7-reasons-why-social-media-artists-are-disrupting-the-advertising-industry-355043aaba67?source=---","https://medium.com/artists-on-the-internet/how-to-be-a-successful-diy-artist-86648df4ffee?source=---","https://medium.com/the-wtf-economy/products-as-art-and-the-manager-as-an-artist-8248d0de672a?source=---","https://medium.com/panel-frame/making-a-comic-book-like-a-movie-an-interview-with-james-zark-about-occult-generation-b0720e9826ec?source=---","https://medium.com/@jeffgoins/why-art-for-art-s-sake-doesn-t-work-9248c409f164?source=---","https://medium.com/vantage/15-instagram-artists-you-should-be-following-24bb63abf415?source=---","https://medium.com/ted-fellows/stormtrooper-in-a-tutu-how-one-russian-artist-is-challenging-stereotypes-in-her-home-country-157788f87a70?source=---","https://medium.com/@saulofhearts/the-perils-of-hope-labor-how-patreon-is-failing-starving-artists-142f8e8ea805?source=---","https://medium.com/life-learning/artists-developers-and-the-deep-structures-of-the-new-world-4dc39f3152e2?source=---","https://medium.com/@kcimc/comparing-artificial-artists-7d889428fce4?source=---","https://medium.com/@bobbie/bowie-was-the-first-artist-i-ever-loved-652a0517fe67?source=---","https://medium.com/@LaughingSquid/artist-illustrates-her-own-cat-in-the-varying-styles-of-famous-comics-and-cartoons-7a3adb4b836b?source=---","https://medium.com/the-coffeelicious/the-epic-and-awesome-guide-to-writing-blog-articles-like-a-true-artist-so-people-want-to-read-your-c13040614b5?source=---","https://medium.com/vantage/the-street-as-school-the-photography-of-alice-smeets-ae85ca6d6dbc?source=---","https://human.parts/i-am-a-professional-tarot-reader-and-not-a-con-artist-7fa923052c26?source=---","https://medium.com/@tylertervooren/how-to-be-an-artist-73f94bd2afcf?source=---","https://medium.com/@johnpavlus/legendary-computer-scientist-alan-kay-on-what-makes-an-artist-180059c44ca2?source=---","https://medium.com/the-limitless-mind/steal-like-an-artist-to-get-some-better-ideas-64c5348f02a9?source=---","https://medium.pjrvs.com/entrepreneur-artist-aee45053a97d?source=---","https://medium.com/@blprnt/an-artist-in-every-library-c0df05bf3c9?source=---","https://human.parts/the-tragedy-of-the-artist-1dbb2b2a2109?source=---","https://medium.com/@LaughingSquid/a-provocative-series-of-embroidered-fashion-photos-that-offer-the-artist-s-alternative-vision-of-8f26226805ce?source=---","https://medium.com/cuepoint/does-a-tidal-wave-lift-all-ships-f663a6fd9aae?source=---","https://medium.com/@evaliparova/why-artists-dont-give-a-crap-about-your-brand-1a89696d4952?source=---","https://medium.com/@valenti/from-here-we-go-ecstatic-4cc632015c7a?source=---","https://medium.com/ios-os-x-development/recreating-spotify-s-tweetbot-s-artist-album-uitableview-8488979fc3e1?source=---","https://medium.com/martin-moore/writers-artists-musicians-photographers-filmmakers-2ce08164b1c6?source=---","https://medium.com/ted-fellows/meet-the-kenyan-artist-turning-nairobi-s-waste-into-eyewear-4a5f5b9d8924?source=---","https://medium.com/@burger/how-your-listening-behavior-pays-artists-on-spotify-9f23ce33c52e?source=---","https://medium.com/ted-fellows/how-one-street-artist-is-spreading-peace-around-the-world-with-arabic-calligraphy-2c89f31e8159?source=---","https://medium.com/@creaturedesigns/the-mind-of-an-artist-9566e77b4ca9?source=---","https://medium.com/@baal.09.tdm/so-you-want-people-to-game-the-system-in-order-to-get-their-favorite-artist-more-money-48361b202460?source=---","https://medium.com/@adammarx13/an-artistic-analysis-of-four-tech-investors-8b2d4a7656e2?source=---","https://medium.com/i-m-h-o/dear-artists-make-me-31b43556ef05?source=---","https://medium.com/hacking-ui/should-designers-learn-code-a-martial-artist-s-approach-b15ae9f1a695?source=---","https://medium.com/robin-sharma-articles/you-are-an-artist-88c37cbc731?source=---","https://medium.com/cuepoint/what-the-blurred-lines-lawyer-taught-all-artists-abc1011d70fd?source=---","https://movingart.depict.com/artist-spotlight-dde4070d639e?source=---","https://medium.com/@lellasa/fiz-a-travessia-larguei-o-emprego-garantido-numa-multinacional-para-ser-artista-pl%C3%A1stico-b6655d6f8a2e?source=---","https://medium.com/ted-fellows/6-artists-who-are-changing-the-way-we-look-at-humanity-d162601338c6?source=---","https://medium.com/@gbaheti/artists-are-hackers-and-hackers-are-artists-9004603774d9?source=---","https://medium.com/@AJEnglish/arab-women-artists-and-their-long-road-to-expression-b1450331a625?source=---","https://medium.com/thursday-notes/are-you-an-artist-336f6099d471?source=---"]
	
	def parse(self, response):
		ts = time.time()
		html_name = 'txt/artist/artist' + str(ts) + '.txt'
		file = codecs.open(html_name, 'w+', 'utf-8')
		
		# file.write(response.url)
		# file.write('\n')

		for body in response.css('div.layoutSingleColumn h3').extract():
			body = body.encode(response.encoding)
			body = remove_tags(body)
			print "Header"
			print(body)
			try:
				file.write(body)
			except AttributeError:
				print(AttributeError)
				sys.exit(0)

		for body in response.css('div.layoutSingleColumn p').extract():
			body = body.encode(response.encoding)
			body = remove_tags(body)
			print "Paragraph"
			print(body)
			try:
				file.write(body)
			except AttributeError:
				print(AttributeError)
				sys.exit(0)

		file.close()