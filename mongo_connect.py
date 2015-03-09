# encoding=utf-8
# __author__ = 'mike'

import pymongo

conn = pymongo.Connection("ec2-54-165-63-201.compute-1.amazonaws.com", 17018)

# 连接库
db = conn['customer-production']

#用户认证
db.authenticate('yplatformprod', 'IRmIeXo7JI')

#打印所有数据
#search_c1 = '"domainNames.hostName":{$exists:true}},{"originServers.portNumber":{$exists:true}'
c_all = db.adns.find()


ydomians = ["www.mothercare.ru",
"www.moosejaw.com",
"www.herrschners.com",
"www.scheels.com",
"www.pureromance.com",
"us.billabong.com",
"www.chadwicks.com",
"www.prana.com",
"www.smartpakequine.com",
"www.thetiebar.com",
"www.livecareer.com",
"www.myperfectresume.com",
"www.macmall.com",
"www.chineselaundry.com",
"www.resume-now.com",
"www.rvca.com",
"www.metrostyle.com",
"uspatriottactical.com",
"www.pcm.com",
"www.home-decorating-co.com",
"www.trxtraining.com",
"www.territoryahead.com",
"www.lehmans.com",
"www.cableorganizer.com",
"www.orientalfurniture.com",
"www.fathead.com",
"eu.billabong.com",
"www.rockcreek.com",
"www.herrschners.ca",
"www.gearhead.com",
"au.billabong.com",
"www.hats.com",
"www.3riversarchery.com",
"tigerlilyswimwear.com.au",
"www.amazonsurf.co.nz",
"ca.billabong.com",
"www.family-nation.it",
"www.pumpunderwear.com",
"www.billabong.com",
"us.vonzipper.com",
"en.worldtempus.com",
"www.dexclusive.com",
"www.kangolstore.com",
"www.zurifurniture.com",
"www.medicalsupplydepot.com",
"www.nationalbusinessfurniture.com",
"www.justforjeeps.com",
"mobile.metrostyle.com",
"fr.worldtempus.com",
"www.livecareer.es",
"www.brits.co.uk",
"rewards.moosejaw.com",
"www.livecareer.fr",
"www.frick.org",
"us.elementbrand.com",
"www.idwholesaler.com",
"www.fenix-store.com",
"www.livecareer.it",
"www.cover-letter-now.com",
"www.from-us.com",
"computer-desks.officefurniture.com",
"www.smileycookie.com",
"www.headsets.com",
"www.premieryarns.com",
"www.officefurniture.com",
"www.dallasmidwest.com",
"www.shopbubba.com",
"www.rockwellnutrition.com",
"www.killcliff.com",
"power.murata.com",
"en.m.worldtempus.com",
"www.yummicandles.com",
"www.fenixoutfitters.com",
"mobile.territoryahead.com",
"www.willowyarns.com",
"www.scentiments.com",
"eu.elementbrand.com",
"puzzleshoppe.herrschners.com",
"www.power.com",
"m.macmall.com",
"www.honoluasurf.com",
"m.trxtraining.com",
"www.officechairs.com",
"www.springerpub.com",
"eu.shop.elementbrand.com",
"www.vology.com",
"www.beckersurf.com",
"ac-dc.power.com",
"www.hylunia.com",
"www.onestopequineshop.com",
"ca.rvca.com",
"www.livecareer.pl",
"www.lifeproof.com",
"fr.m.worldtempus.com",
"www.hubcapzone.com",
"ca.vonzipper.com",
"office-desks.nationalbusinessfurniture.com",
"yarnsale.herrschners.com",
"www.cnvc.org",
"www.pumpunderwear.eu",
"www.idzone.com",
"home-office-furniture.officefurniture.com",
"www.nationalbusinessfurniture.ca",
"www.arcona.com",
"au.elementbrand.com",
"willowyarns.herrschners.com",
"br.billabong.com",
"www.imprivata.com",
"www.cactustactical.com",
"tables.dallasmidwest.com",
"bookcases.nationalbusinessfurniture.com",
"www.fireflybuys.com",
"wireless.murata.com",
"www.knobbery.com",
"reception-furniture.officefurniture.com",
"office-chairs.nationalbusinessfurniture.com",
"ergonomic-chairs.officechairs.com",
"all-office-chairs.officechairs.com",
"www.walleyedirect.com",
"www.pumpunderwear.fr",
"ca.elementbrand.com",
"www.shopping-bargains.com",
"www.nichemodern.com",
"storage-cabinets.officefurniture.com",
"www.family-nation.com",
"www.yottaa.com",
"www.pumpunderwear.co.uk",
"www.resume-check.com",
"www.premieryarns.ca",
"responsibility-project.libertymutual.com",
"www.willowyarns.ca",
"www.greekgear.com",
"office-tables.officefurniture.com",
"blog.macmall.com",
"leather-chairs.officechairs.com",
"office-chairs.officefurniture.com",
"led-driver.power.com",
"puzzleshoppe.herrschners.ca",
"store.cableorganizer.com",
"www.elementjapan.com",
"executive-chairs.officechairs.com",
"office-tables.nationalbusinessfurniture.com",
"file-cabinets.nationalbusinessfurniture.com",
"office-storage.nationalbusinessfurniture.com",
"breakroom-furniture.nationalbusinessfurniture.com",
"www.topknobsandpulls.com",
"jp.vonzipper.com",
"boards.dallasmidwest.com",
"www.1800headsets.ca",
"reception-chairs.officechairs.com",
"igbt-driver.power.com",
"www.dealmed.com",
"file-cabinets.officefurniture.com",
"eu.elementeden.com",
"bd.pcm.com",
"willowyarns.herrschners.ca",
"school-furniture.dallasmidwest.com",
"together.cigna.com",
"bookcases.officefurniture.com",
"all-office-furniture.officefurniture.com",
"all-office-furniture.nationalbusinessfurniture.com",
"office-desks.nationalbusinessfurniture.ca",
"computer-chairs.officechairs.com",
"chairs-seating.dallasmidwest.com",
"big-and-tall-chairs.officechairs.com",
"au.vonzipper.com",
"yarnsale.herrschners.ca",
"task-chairs.officechairs.com",
"au.rvca.com",
"conference-furniture.nationalbusinessfurniture.com",
"prodtest.macmall.com",
"office-chairs.nationalbusinessfurniture.ca",
"desks.dallasmidwest.com",
"www.hhcc.com",
"reception-furniture.nationalbusinessfurniture.com",
"image1.cc-inc.com",
"www.eagleinvsys.com",
"www.stonefirms.com",
"www.weddingstar.com",
"office-furniture.dallasmidwest.com",
"office-accessories.nationalbusinessfurniture.com",
"rwz.myperfectresume.com",
"tv-stands.officefurniture.com",
"www.ebags.com",
"office-partitions.nationalbusinessfurniture.com",
"www.cr123batteries.com",
"www.lotussculpture.com",
"www.livecareer.de",
"www.coachwei.com",
"test.prana.com",
"eu.rvca.com",
"church-furniture.dallasmidwest.com",
"resume.livecareer.com",
"mesh-chairs.officechairs.com",
"www.clarksusa.com",
"office-accessories.officefurniture.com",
"jp.rvca.com",
"eu.vonzipper.com",
"conference-chairs.officechairs.com",
"www.projetoresponsabilidade.com.br",
"all-furniture.dallasmidwest.com",
"conference-room-furniture.officefurniture.com",
"resumes.livecareer.com",
"filing-cabinets.nationalbusinessfurniture.ca",
"office-tables.nationalbusinessfurniture.ca",
"www.pcmg.com",
"drafting-chairs-and-stools.officechairs.com",
"office-collections.nationalbusinessfurniture.com",
"store.taylorswift.com",
"za.rvca.com",
"www.brighterblooms.com",
"kidstuff.com.au",
"www.pumpunderwear.es",
"computer-armoires.officefurniture.com",
"bd.macmall.com",
"www.proyectoresponsabilidad.co",
"bookcases.nationalbusinessfurniture.ca",
"www.diningbycandlelight.com",
"www.proyectoresponsabilidad.cl",
"www.burlingtoncoatfactory.com",
"office-storage.nationalbusinessfurniture.ca",
"av-equipment.dallasmidwest.com",
"tv-stands.nationalbusinessfurniture.ca",
"breakroom-furniture.officefurniture.com",
"office-partitions.officefurniture.com",
"www.jbugs.com",
"www.proyectoresponsabilidad.com.ve",
"lobby-furniture.dallasmidwest.com",
"prodtest.pcm.com",
"engage.cabinetoffice.gov.uk",
"training-furniture.nationalbusinessfurniture.com",
"www.solutionsirb.com",
"blog.pcm.com",
"chair-mats.officechairs.com",
"storage-filing.dallasmidwest.com",
"mediafirst.net",
"engage.number10.gov.uk",
"childhood-daycare.dallasmidwest.com",
"www.pumpunderwear.co",
"www.thebodyshop.ru",
"www.maperformance.com",
"m.lifeproof.com",
"www.smcpneumatics.com",
"partitions.dallasmidwest.com",
"library-furniture.dallasmidwest.com",
"guest-chairs.officechairs.com",
"partitions.nationalbusinessfurniture.ca",
"caddies-dollies.dallasmidwest.com",
"www.hobbytown.com",
"www.nation.co.ke",
"www.exfo.com",
"stages-risers.dallasmidwest.com",
"i2.cc-inc.com",
"www.livecareer.nl",
"www.macmallretail.com",
"nspi.pcm.com",
"www.solutionsinstitute.com",
"www.7diamonds.com",
"office-accessories.nationalbusinessfurniture.ca",
"www.thephoneleash.com",
"www.thewatchprince.com",
"www.gemplers.com",
"tests.livecareer.com",
"bd.pcmg.com",
"www.topatoco.com",
"www.worldtempus.com",
"technovangelist.com",
"www.fastfollowerz.com",
"www.yeswellness.com",
"www.sheetmusicplus.com",
"www.technologyreview.com",
"www.us-mattress.com",
"www.heels.com",
"edgecast-ab-testing",
"www.sonosite.com",
"www.serenaandlily.com",
"www.muthuhotels.com",
"www.stylinonline.com",
"warranty.billabong-usa.com",
"johnedward.net",
"www.flooringsupplies.co.uk",
"www.marketviewliquor.com",
"www.steripen.com",
"bostonian.clarksusa.com",
"www.ecost.com",
"aspdotnetstorefront.lehmans.com",
"natostrapsco.com",]
# c1 = db.adns.find({"domainNames.active": True})
#adns = db.adns.find({"domainNames.hostName": "www.macmall.com", "isDeleted": False})
adns = db.adns.find({"isDeleted": False})
# adns = db.adns.find()

print 'start1'

for adn in adns:

    if not adn.has_key("originServers"):
        continue
    if not adn.has_key("loadBalancers"):
        continue
    if not adn.has_key("domainNames"):
        continue

    all_os = adn["originServers"]
    all_lb = adn["loadBalancers"]
    all_dm = adn["domainNames"]

    for dm in all_dm:
        if not dm["active"]:
            continue
        for os in all_os:
            if not os["_id"]:
                continue
            if dm["target"].has_key('idref') and dm["target"]["idref"] == os["_id"]:
                if not os["ipAddress"]:
                    os["ipAddress"] = '------------'
                if not os["hostName"]:
                    os["hostName"] = '------------'
                for yd in ydomians:
                    if yd == dm["hostName"]:
                        print dm["hostName"] + "," + os["ipAddress"] + "," + os["hostName"]
print 'end1'
# print 'start2'
#
# for adn in adns:
#
#     if not adn.has_key("originServers"):
#         continue
#     if not adn.has_key("loadBalancers"):
#          continue
#     if not adn.has_key("domainNames"):
#         continue

#    print 'adn'
#    print adn

#     all_os = adn["originServers"]
#     all_lb = adn["loadBalancers"]
#     all_dm = adn["domainNames"]
#
#     for dm in all_dm:
#         if not dm["active"]:
#             continue
#         for lb in all_lb:
#             for lb_member in lb["members"]:
#                 for os in all_os:
#                     if not os["_id"]:
#                         continue
#                     print "1  -->  " + lb_member["idref"]
#                     print "2  -->  " + os["_id"]
#                     if lb_member["idref"] in  ["us","eu","ap","sa"]:
#                         continue
#                     if lb_member["idref"] and lb_member["idref"] == os["_id"]:
#
#                         if not os["ipAddress"]:
#                             os["ipAddress"] = '------------'
#                         if not os["hostName"]:
#                             os["hostName"] = '------------'
#                         for yd in ydomians:
#                             if yd == dm["hostName"]:
#                                 print dm["hostName"] + "\t\t" + os["ipAddress"] + "\t\t" + os["hostName"]
#
#
# print 'end2'