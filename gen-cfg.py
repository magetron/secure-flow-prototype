from staticfg import CFGBuilder

userCfg = CFGBuilder().build_from_file('user.py', './auction/user.py')
bidCfg = CFGBuilder().build_from_file('bid.py', './auction/bid.py')
auctionCfg = CFGBuilder().build_from_file('auction.py','./auction/auction.py')

#auctionEventCfg = CFGBuilder().build_from_file('auction_event.py','./auction/auction_event.py')

bidCfg.build_visual('bidCfg', 'pdf')
auctionCfg.build_visual('auctionCfg', 'pdf')
#auctionEventCfg.build_visual('auctionEventCfg.pdf', 'pdf')
