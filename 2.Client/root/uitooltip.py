## 1.) Find this:
	def AppendWearableInformation(self):
		[...]


## 2.) Replace with this:
	if app.ENABLE_ANTIFLAG_WEARABLE:
		def AppendWearableInformation(self):
			antiFlagJobSexDict = {
					localeInfo.TOOLTIP_ANTIFLAG_MALE		: item.IsAntiFlag(item.ITEM_ANTIFLAG_FEMALE),
					localeInfo.TOOLTIP_ANTIFLAG_FEMALE		: item.IsAntiFlag(item.ITEM_ANTIFLAG_MALE),
			}
			antiFlagJobDict = {
					localeInfo.TOOLTIP_ANTIFLAG_WARRIOR		: not item.IsAntiFlag(item.ITEM_ANTIFLAG_WARRIOR),
					localeInfo.TOOLTIP_ANTIFLAG_ASSASSIN	: not item.IsAntiFlag(item.ITEM_ANTIFLAG_ASSASSIN),
					localeInfo.TOOLTIP_ANTIFLAG_SURA		: not item.IsAntiFlag(item.ITEM_ANTIFLAG_SURA),
					localeInfo.TOOLTIP_ANTIFLAG_SHAMAN		: not item.IsAntiFlag(item.ITEM_ANTIFLAG_SHAMAN),
			}
			self.AppendSpace(5)
			self.AppendHorizontalLine()
			textLine = self.AppendTextLine(localeInfo.TOOLTIP_ANTILAG_WEARABLE_JOB, self.TITLE_COLOR, True)

			antiFlagJobSexNames	= [name for name, flag in antiFlagJobSexDict.iteritems() if flag]
			antiFlagJobNames	= [name for name, flag in antiFlagJobDict.iteritems() if flag]

			if antiFlagJobSexNames:
				self.AppendSpace(1)
				textLine = self.AppendTextLine('{} {}'.format(', '.join(antiFlagJobSexNames), ''), self.CONDITION_COLOR)

			if antiFlagJobNames:
				self.AppendSpace(3)
				textLine = self.AppendTextLine('{} {}'.format(', '.join(antiFlagJobNames), ''), self.CONDITION_COLOR)

			textLine.SetFeather()
	else:
		def AppendWearableInformation(self):
			self.AppendSpace(5)
			self.AppendTextLine(localeInfo.TOOLTIP_ITEM_WEARABLE_JOB, self.NORMAL_COLOR)

			flagList = (
				not item.IsAntiFlag(item.ITEM_ANTIFLAG_WARRIOR),
				not item.IsAntiFlag(item.ITEM_ANTIFLAG_ASSASSIN),
				not item.IsAntiFlag(item.ITEM_ANTIFLAG_SURA),
				not item.IsAntiFlag(item.ITEM_ANTIFLAG_SHAMAN))

			characterNames = ""
			for i in xrange(self.CHARACTER_COUNT):

				name = self.CHARACTER_NAMES[i]
				flag = flagList[i]

				if flag:
					characterNames += " "
					characterNames += name

			textLine = self.AppendTextLine(characterNames, self.NORMAL_COLOR, True)
			textLine.SetFeather()

			if item.IsAntiFlag(item.ITEM_ANTIFLAG_MALE):
				textLine = self.AppendTextLine(localeInfo.FOR_FEMALE, self.NORMAL_COLOR, True)
				textLine.SetFeather()

			if item.IsAntiFlag(item.ITEM_ANTIFLAG_FEMALE):
				textLine = self.AppendTextLine(localeInfo.FOR_MALE, self.NORMAL_COLOR, True)
				textLine.SetFeather()


