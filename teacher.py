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
	start_urls = ["https://medium.com/synapse/an-open-letter-to-my-sons-kindergarten-teacher-ed1f90239ae7?source=false---------1","https://medium.com/addiction-unscripted/confessions-of-a-drug-addicted-high-school-teacher-d41a15bd1170?source=false---------2","https://medium.com/synapse/why-i-got-rid-of-my-teacher-s-desk-4b47b814b34?source=false---------3","https://medium.com/@dushkazapata/teacher-af975af1c369?source=false---------4","https://medium.com/age-of-awareness/what-a-substitute-teacher-taught-me-about-leaving-a-legacy-e76b8205129e?source=false---------5","https://medium.com/@bennettscience/teacher-6ebba9728c7a?source=false---------6","https://medium.com/@FUSIONry/let-your-actions-speak-on-your-behalf-and-not-by-force-imposing-the-attitude-of-teacher-and-fear-to-865a64e5a85e?source=false---------7","https://medium.com/@Smritiyoga/what-does-it-take-to-be-a-yoga-teacher-c521633a06e4?source=false---------8","https://medium.com/@evadestruktion/a-great-teacher-died-and-i-missed-my-chance-to-say-thank-you-29639ca2bb8b?source=false---------9","https://medium.com/@mikepaul/my-friend-the-first-year-teacher-55ee58844045?source=false---------10","https://medium.com/@rebeccaberlinfield/teacher-fb1070e8db25?source=---","https://medium.com/@tapansharma/teacher-48581b7c73e8?source=---","https://medium.com/@kellilycke/anyone-know-who-the-bald-headed-teacher-is-w4m-636de2914b12?source=---","https://medium.com/@cho2351/teacher-fa1052769422?source=---","https://medium.com/@PallComms/when-the-student-is-ready-the-teacher-is-there-love-this-thank-you-f4dc22d464b9?source=---","https://medium.com/@growthmindset2/a-teacher-is-also-a-student-d497f928f805?source=---","https://medium.com/@viralVidsnMore/video-nursery-teacher-s-double-life-caught-on-hidden-camera-3f8074485c83?source=---","https://medium.com/@SRIMISSION/virtues-of-a-teacher-24ea5cd18886?source=---","https://medium.com/@getprocopy/5-teacher-top-tips-on-writing-1e127d2cdf02?source=---","https://talk.chalk.com/the-most-and-least-paid-teachers-in-the-world-76e312dc2cd1?source=---","https://medium.com/bright/millions-of-teachers-minting-millionaire-teachers-decc4fe41604?source=---","https://medium.com/bright/automated-teachers-augmented-reality-and-floating-chairs-6a71fc7cf296?source=---","https://medium.com/bright/here-s-a-way-to-help-teachers-f3b04c111cf0?source=---","https://medium.com/@helenab/so-i-m-a-teacher-now-ten-reflections-from-the-first-ten-weeks-c697e9cf5f80?source=---","https://medium.com/bright/my-fifth-grade-teacher-fedc4a20191d?source=---","https://medium.com/bright/the-striking-similarities-between-teachers-and-start-up-ceos-29169a462b46?source=---","https://medium.com/bright/ipads-teachers-e51896af3930?source=---","https://thsppl.com/teachers-in-nypd-shirts-racists-or-heroes-a4e389cf1e32?source=---","https://medium.com/@sgblank/mentors-coaches-and-teachers-7025749174d3?source=---","https://medium.com/@philipkovacs/a-response-to-a-parent-from-a-kindergarten-teacher-e2e06393a5e4?source=---","https://medium.com/bright/middle-school-as-seen-through-the-eyes-of-teachers-cell-phone-b9aefda5c047?source=---","https://medium.com/bright/a-smarter-way-to-teach-the-teachers-8a4cedbf060e?source=---","https://medium.com/@amandaripley/the-smartest-teachers-in-the-world-cd5e10a902b6?source=---","https://medium.com/@AmyJoMartin/my-teacher-didn-t-show-up-today-it-was-the-best-lesson-ever-1560453e377e?source=---","https://medium.com/synapse/10-things-your-are-unlikely-to-hear-as-an-elementary-school-teacher-883ec46147ab?source=---","https://medium.com/@mpstenson/here-s-the-true-problem-no-matter-what-you-want-to-argue-about-equivalence-the-teacher-s-feedback-71fea6830c04?source=---","https://medium.com/bright/how-we-can-elevate-teachers-2082603a1bbc?source=---","https://medium.com/bright/teacher-and-the-machine-1d05f41c3572?source=---","https://human.parts/my-life-and-times-as-a-closeted-seventh-grade-teacher-fae590bdab9b?source=---","https://medium.com/synapse/me-ava-which-of-your-teachers-would-survive-a-zombie-apocalypse-978d0d49af9e?source=---","https://medium.com/matter/kenya-s-teachers-knew-they-were-being-targeted-by-terrorists-nobody-listened-3cc8e37538d9?source=---","https://medium.com/keep-learning-keep-growing/the-teacher-the-engineer-and-the-mad-scientist-2e05ba73b8f3?source=---","https://medium.com/@karnul/growing-up-as-a-gifted-child-where-i-knew-all-the-answers-and-corrected-the-teachers-from-time-to-ab6e0633238f?source=---","https://medium.com/synapse/student-centered-vs-teacher-centered-learning-2184a7521720?source=---","https://medium.com/the-huffington-post/america-s-best-history-teacher-doesn-t-work-at-a-school-1c8717b53d96?source=---","https://medium.com/synapse/teachers-using-twitter-1a6905fdda61?source=---","https://medium.com/bright/this-is-how-some-of-america-s-best-teachers-spend-their-time-4a0ded0fbb56?source=---","https://medium.com/bright/a-teacher-s-take-on-a-geeky-education-tech-conference-d54df495835e?source=---","https://medium.com/synapse/what-makes-an-all-star-teacher-514e16db29a2?source=---","https://human.parts/i-wish-i-didn-t-want-to-be-a-teacher-319bbf96c81e?source=---","https://medium.com/the-limitless-mind/what-our-parents-and-teachers-never-told-us-about-failure-b0544f5b425c?source=---","https://medium.com/bright/what-do-teachers-do-after-saying-goodbye-to-the-classroom-a8566cb29f77?source=---","https://medium.com/synapse/the-problem-with-twenty-somethings-teachers-c1674696a58?source=---","https://medium.com/@susancain/how-do-teachers-feel-about-their-quiet-students-e8c58839d3dd?source=---","https://medium.com/synapse/5-things-you-won-t-learn-in-teachers-college-a546df843109?source=---","https://medium.com/@shubberali/my-high-school-calculus-teacher-had-a-simple-solution-for-this-in-the-1980s-he-made-everything-c2aef8f3e868?source=---","https://medium.com/@markgonyea/i-am-a-high-school-calculus-teacher-and-i-fight-with-my-students-to-put-their-calculators-away-128d5423b138?source=---","https://medium.com/synapse/10-lessons-from-dumbledore-for-teachers-and-parents-2e8586ec0fe3?source=---","https://medium.com/synapse/no-for-what-it-s-worth-i-m-a-former-math-teacher-and-i-appreciate-brett-s-effort-to-encourage-9b644ae9348?source=---","https://medium.com/bright/ahoy-meet-nancy-davis-the-pirate-teacher-video-86adaaa0a57b?source=---","https://medium.com/bright/how-can-we-bring-teachers-along-for-the-ride-797f0b7c82d6?source=---","https://medium.com/the-lighthouse/the-stiffest-yoga-teacher-in-l-a-326914e1258a?source=---","https://medium.com/life-learning/your-polisci-teacher-was-wrong-people-aren-t-inherently-evil-b52474ce55af?source=---","https://medium.com/bright/great-teachers-are-not-built-overnight-e03b40a74586?source=---","https://medium.com/synapse/10-things-teachers-should-know-about-spotify-234ff848ca35?source=---","https://medium.com/synapse/new-teacher-advice-dress-the-part-67300c56c97c?source=---","https://medium.com/synapse/a-note-on-teacher-certification-2a6c2df499d2?source=---","https://medium.com/reporters-notebook/need-is-a-very-good-teacher-1e0a14f247d4?source=---","https://medium.com/@chrisjagers/the-teacher-learns-the-most-df4d9a54706?source=---","https://medium.com/change-maker/empowering-teachers-to-empower-young-people-5cbb05f7b0db?source=---","https://medium.com/synapse/a-terrible-teacher-tells-all-d82bbf1a6f79?source=---","https://medium.com/synapse/5-ways-teachers-can-fight-the-power-5895215ff6cf?source=---","https://medium.com/@ericworral_33053/iowa-music-teacher-suspended-for-inciting-lunch-room-riot-778aff6a5c9b?source=---","https://medium.com/bright/teaching-the-teachers-140-characters-at-a-time-6659d9db8bf3?source=---","https://medium.com/@harrymlevine/a-teachers-two-cents-when-learning-ruby-on-rails-cf51808581d4?source=---","https://medium.com/prospect-innovators/look-how-hs-writing-teachers-can-use-medium-5fa90f3c6400?source=---","https://higheredrevolution.com/considering-forcing-teachers-to-use-technology-think-again-eacdbbf70e6e?source=---","https://medium.com/bright/three-easy-tips-for-teachers-on-twitter-ee2575cb835b?source=---","https://medium.com/from-a-teacher/forbes-created-a-30-under-30-list-for-education-included-exactly-zero-k-12-teachers-6046d25c4024?source=---","https://medium.com/@gracemcmc/the-other-day-i-heard-a-story-about-one-of-the-teachers-in-my-school-that-repulsed-me-be90be37e593?source=---","https://medium.com/switch-collective/even-teachers-should-be-able-to-switch-675490c6d36b?source=---","https://higheredrevolution.com/educational-technology-trends-what-teachers-should-know-b26b5672297?source=---","https://medium.com/bright/treating-student-teachers-like-doctors-in-training-caa1068f4016?source=---","https://medium.com/synapse/can-you-be-a-teacher-and-a-friend-1adb871b94cb?source=---","https://medium.com/synapse/why-do-teachers-quit-cfb3f3ab67b7?source=---","https://context.newamerica.org/could-micro-credentials-drive-transparency-and-quality-in-teacher-learning-6ffcf2b7512b?source=---","https://medium.com/bright/how-do-we-build-a-truly-diverse-teacher-workforce-20d77956f3f9?source=---","https://medium.com/synapse/what-if-teachers-were-treated-like-startup-founders-4dc84cf70b5a?source=---","https://medium.com/synapse/i-m-a-teacher-what-s-your-super-power-d999c6fc4391?source=---","https://medium.com/@InVisionApp/how-design-teachers-approach-design-in-the-classroom-5fc3c48a6e1c?source=---","https://medium.com/synapse/teacherpreneurs-changing-education-from-the-inside-out-ad83c2442?source=---","https://medium.com/@norman_tran/open-love-letter-to-teachers-guild-852eb3a8ee1b?source=---","https://medium.com/from-a-teacher/working-and-learning-with-a-teacher-people-gave-up-on-a432641ddc3f?source=---","https://medium.com/synapse/teachers-as-researchers-fe9d19c98be8?source=---","https://medium.com/@MatthewRMorris/things-teachers-tell-students-but-don-t-do-themselves-805e797a0ab7?source=---","https://medium.com/@Brookings/can-every-student-have-an-equal-chance-at-a-great-teacher-cb4d640f841f?source=---","https://medium.com/teachersguild/the-teachers-guild-book-club-97de5d38f1d3?source=---","https://medium.com/the-coffeelicious/so-your-sex-ed-teacher-is-a-rapist-b393feb5f85d?source=---","https://medium.com/synapse/why-teachers-should-strive-to-be-like-mr-keating-27a03fa6cbe6?source=---","https://medium.com/copyright-untangled/dear-teacher-copyright-concerns-you-829b2f33174c?source=---","https://medium.com/@intel/helping-teachers-plug-kids-into-the-maker-movement-ae6dcb55de23?source=---","https://medium.com/synapse/teacher-voice-dropping-the-mic-to-make-sure-its-broke-f60164c58ecc?source=---","https://medium.com/synapse/the-one-thing-no-new-teacher-has-to-worry-about-17fd53b1ac5b?source=---","https://medium.com/bright/teacher-abuse-the-actions-and-reactions-are-the-real-story-b9e54f630578?source=---","https://medium.com/i-love-charts/word-roots-a-students-and-teachers-best-friend-c43bf389142f?source=---","https://medium.com/synapse/can-online-learning-make-us-better-teachers-9c452fd14ad0?source=---","https://medium.com/bright/most-sexuality-teachers-know-what-good-sex-ed-is-we-are-just-not-allowed-to-teach-it-648cf59da67d?source=---","https://medium.com/synapse/the-perfect-teacher-e8159baa476c?source=---","https://medium.com/tntp-ideas-research-and-opinion/teacher-prep-what-s-data-got-to-do-with-it-1c3ccd44e388?source=---","https://medium.com/synapse/how-not-to-micromanage-as-a-teacher-f04e57a64a5f?source=---","https://medium.com/@NSF/real-talk-from-computer-science-teachers-89c935346ff2?source=---","https://medium.com/@thelizard/it-shows-the-children-that-unless-they-do-the-problem-exactly-the-way-the-teacher-wants-they-are-772d01ae01cf?source=---","https://medium.com/synapse/5-things-every-teacher-should-do-during-summer-break-8fd9630d96c2?source=---","https://medium.com/synapse/why-can-t-they-make-it-easier-to-become-a-teacher-b25ea3415a6?source=---","https://medium.com/@m_nebra/teachers-tell-them-they-re-good-even-if-they-re-not-cd71bbefca3?source=---","https://medium.com/synapse/personalized-learning-for-teachers-5fdb155b8fed?source=---","https://medium.com/bright/as-an-attendee-of-the-i3-event-at-medium-i-was-struck-by-the-fact-i-was-the-only-teacher-in-the-868331326469?source=---","https://medium.com/synapse/time-for-teachers-to-prepare-their-future-colleagues-ceddf5f5a2a?source=---","https://medium.com/synapse/10-things-you-are-unlikely-to-hear-a-teacher-say-on-a-wednesday-evening10-things-you-are-unlikely-eecb2086a1c4?source=---","https://medium.com/synapse/the-absence-of-teachers-of-color-isn-t-just-a-problem-for-non-white-students-it-s-a-problem-for-c72b1235a564?source=---","https://medium.com/@morganlinton/an-open-letter-to-my-high-school-geometry-teacher-f24671104488?source=---","https://medium.com/synapse/who-rates-teachers-this-way-e1758db02655?source=---","https://medium.com/the-linguist-on-language/do-we-need-a-teacher-when-learning-a-new-language-9f8140935e44?source=---","https://medium.com/synapse/what-type-of-teacher-are-you-271d1cf034b4?source=---","https://medium.com/synapse/teachers-add-technology-to-your-classroom-the-right-way-98acdb46ede7?source=---","https://medium.com/from-a-teacher/or-a-teacher-6b1204713e7e?source=---","https://medium.com/alt-ledes/leaders-in-my-state-are-playing-politics-at-the-expense-of-teachers-students-and-our-reputation-732b8fb05820?source=---","https://medium.com/@DanWeisbergTNTP/building-a-better-teacher-from-day-one-24e3f4b80305?source=---","https://medium.com/verses-education/what-teachers-need-to-know-about-snapchat-1f0421a15738?source=---","https://medium.com/teachersguild/pia-a-learning-specialist-6014c9516db2?source=---","https://medium.com/@SteveSaul82/5-education-apps-teachers-can-be-thankful-for-in-2015-cc6cc37ccb8d?source=---","https://medium.com/synapse/reason-4-teacher-autonomy-over-best-practices-1fe795ed9f0c?source=---","https://medium.com/synapse/bridging-parents-and-teachers-1c5e23d129c1?source=---","https://medium.com/synapse/doing-good-work-vs-pleasing-the-teacher-19205ec54826?source=---","https://medium.com/from-a-teacher/here-are-10-reasons-there-will-never-be-a-teacher-drafted-to-public-education-3df50aec51f1?source=---","https://medium.com/the-unlisted/giving-back-to-teachers-in-need-fcd029f49e51?source=---","https://medium.com/the-future-of-education/teachers-as-seals-of-the-classroom-998d4550faac?source=---","https://medium.com/ones-space/the-honduran-activists-who-busted-thousands-of-ghost-teachers-a5cae634ed11?source=---","https://medium.com/synapse/to-revolutionize-pd-administrators-should-follow-this-simple-rule-think-like-a-teacher-2cda645f3f97?source=---","https://medium.com/synapse/idle-confessions-of-a-teacher-trying-something-new-6897399ddf50?source=---","https://medium.com/ionic-and-the-mobile-web/a-former-teacher-s-musings-on-open-source-and-web-technologies-fe9fae4b310a?source=---","https://medium.com/synapse/spotlight-on-innovation-computer-programming-teacher-paul-hennig-f6c3af1d0110?source=---","https://medium.com/life-tips/solitude-is-a-good-teacher-76e2b25b3afa?source=---","https://medium.com/@georgekao/if-you-re-stuck-creating-content-remember-the-ceramics-teacher-7dca1ca9b2a4?source=---","https://medium.com/@The74/2-new-reports-show-that-we-really-don-t-have-a-great-way-to-evaluate-teachers-27f01528e021?source=---","https://medium.com/teachersguild/how-two-teachers-enabled-me-to-rediscover-my-intellectual-curiosity-954342ec00a4?source=---","https://higheredrevolution.com/teachers-vs-everybody-48e2e2533f3a?source=---","https://medium.com/@michellestone/as-a-pre-school-teacher-and-a-mom-your-story-pushed-so-many-of-my-buttons-on-so-many-levels-15842a093c7?source=---","https://medium.com/@tfarley1969/pta-is-opting-out-of-their-affiliation-with-parents-and-teachers-9ceb11b9e738?source=---","https://medium.com/@kategeiselman/here-s-a-grammar-lesson-from-the-english-teacher-9ef00421f435?source=---","https://medium.com/synapse/what-type-of-teacher-are-you-part-2-e6e2eb56a271?source=---","https://medium.com/@morganlinton/what-my-8th-grade-science-teacher-taught-me-about-life-dcaac641017d?source=---","https://medium.com/teachersguild/how-two-teachers-are-radically-collaborating-ff90dcfd4c6?source=---","https://medium.com/@mapelen/are-digital-tools-for-teachers-the-key-to-school-2-0-15ee2f5c80dc?source=---","https://medium.com/homeland-security/what-parents-should-tell-their-kids-about-school-shootings-fa53975cf82b?source=---","https://medium.com/@therealalexmay/the-substitute-teachers-manifesto-64276f9446f4?source=---","https://medium.com/synapse/the-ultimate-teacher-types-b4356e960941?source=---","https://medium.com/synapse/three-ways-to-help-teachers-use-research-1dab8d88d382?source=---","https://medium.com/synapse/a-counter-narrative-to-the-myth-of-the-hero-teacher-cc5dc178af73?source=---","https://medium.com/synapse/globally-competent-students-require-globally-competent-teachers-833420205395?source=---","https://medium.com/@Indie_Educator/the-discipline-of-inspiration-for-montessori-teachers-f045024b4630?source=---","https://medium.com/@ThingstoDoInSG/what-downward-dog-pose-tells-us-yoga-teachers-about-you-may-shock-you-6c1c3408e384?source=---","https://talk.chalk.com/the-no-teacher-left-behind-act-4816b9f7a0f4?source=---","https://medium.com/tntp-ideas-research-and-opinion/these-great-teachers-only-spend-half-their-time-teaching-cdccd2a4f56?source=---","https://medium.com/@fjmubeen/the-teacher-of-tomorrow-will-be-neither-human-nor-machine-f9433139ee16?source=---","https://medium.com/@iAmKeanna/this-is-beautiful-i-was-once-a-teacher-i-can-only-hope-i-was-someone-s-phyllis-a3d36dcaddbd?source=---","https://medium.com/donorschoose-org-stories/virginia-teacher-helps-joplin-rebuild-a1fad6d45429?source=---","https://medium.com/teachersguild/one-teacher-s-journey-to-becoming-a-teacher-designer-89639681b7e3?source=---","https://medium.com/from-a-teacher/what-do-you-wish-you-would-ve-known-before-becoming-a-teacher-527dd8e71e4c?source=---","https://medium.com/@tylertervooren/hot-dogs-and-economics-how-great-teachers-guarantee-learning-39ff33540be1?source=---","https://talk.chalk.com/teachers-in-new-york-earn-90-more-than-in-south-dakota-56421747a7b1?source=---","https://medium.com/@rlaracuente/so-sad-that-a-teacher-s-salary-is-synonymous-with-dirt-cheap-pay-12943aa18c63?source=---","https://medium.com/synapse/a-letter-to-my-daughter-s-future-teacher-df5288d09920?source=---","https://medium.com/synapse/teachers-and-education-researchers-a-relationship-which-needs-to-change-9957111f9eaa?source=---","https://medium.com/synapse/how-to-advocate-for-teachers-4ecedf7d3c12?source=---","https://medium.com/@cfbolduc/from-spanish-teacher-to-community-manager-62dca47b4806?source=---","https://medium.com/@StudentsFirst/california-tenure-ruling-is-a-win-for-students-and-teachers-1ea634dcbe93?source=---","https://medium.com/synapse/how-to-fix-the-teacher-auditing-conundrum-216b400fe7c7?source=---","https://medium.com/synapse/how-to-impress-your-teacher-dda351790123?source=---","https://medium.com/@AlessiAnniballo/my-teacher-told-me-i-was-not-good-at-writing-so-i-became-a-journalist-5d686a3d29bd?source=---","https://medium.com/synapse/value-added-measures-vams-do-not-measure-teacher-effectiveness-c830e5b89a2a?source=---","https://medium.com/@teachingquality/are-teachers-unwilling-to-change-7d0167c817e2?source=---","https://medium.com/@uncollege/how-a-teacher-inspired-me-to-leave-school-4f8f15e9970f?source=---","https://medium.com/@abdikhalikovaa/i-asked-a-question-one-of-the-best-teachers-in-university-beab2889dde1?source=---","https://medium.com/@heathmcrigsby/aww-did-the-teacher-hurt-the-little-sheboon-s-feefees-57bd739c5653?source=---"]
	
	def parse(self, response):
		ts = time.time()
		html_name = 'txt/teacher/teacher' + str(ts) + '.txt'
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