
class HeroFeatureExtractor(object):
    """Extract features related to a hero."""

    HEROES = ['Abaddon','Alchemist','Ancient Apparition','Anti Mage','Arc Warden','Axe','Bane','Batrider','Beastmaster','Bloodseeker','Bounty Hunter','Brewmaster','Bristleback','Broodmother','Centaur Warrunner','Chaos Knight','Chen','Clinkz','Clockwerk','Crystal Maiden','Dark Seer','Dazzle','Death Prophet','Disruptor','Doom','Dragon Knight','Drow Ranger','Earth Spirit','Earthshaker','Elder Titan','Ember Spirit','Enchantress','Enigma','Faceless Void','Gyrocopter','Huskar','Invoker','Io','Jakiro','Juggernaut','Keeper of the Light','Kunkka','Legion Commander','Leshrac','Lich','Lifestealer','Lina','Lion','Lone Druid','Luna','Lycan','Magnus','Medusa','Meepo','Mirana','Morphling','Naga Siren','Natures Prophet','Necrophos','Night Stalker','Nyx Assassin','Ogre Magi','Omniknight','Oracle','Outworld Devourer','Phantom Assassin','Phantom Lancer','Phoenix','Pit Lord','Puck','Pudge','Pugna','Queen of Pain','Razor','Riki','Rubick','Sand King','Shadow Demon','Shadow Fiend','Shadow Shaman','Silencer','Skywrath Mage','Slardar','Slark','Sniper','Spectre','Spirit Breaker','Storm Spirit','Sven','Techies','Templar Assassin','Terrorblade','Tidehunter','Timbersaw','Tinker','Tiny','Treant Protector','Troll Warlord','Tusk','Undying','Ursa','Vengeful Spirit','Venomancer','Viper','Visage','Warlock','Weaver','Windranger','Winter Wyvern','Witch Doctor','Wraith King','Zeus']

    @classmethod
    def extract(cls, hero_name_str):
        """Returns attributes related to a particular hero."""
        features = list()

        features.append(cls.getHeroIndex(hero_name_str))

        return features

    @classmethod
    def getHeroIndex(cls, hero_name_str):
        """Returns the index of the hero in the hero list."""
        return float(cls.HEROES.index(hero_name_str))