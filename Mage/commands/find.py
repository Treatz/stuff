from evennia.commands.default.muxcommand import MuxCommand


class CmdFind(MuxCommand):
    key = "+locate"
    locks = "cmd:all()"
    def func(self):
        skip = 1
        for ishere in self.caller.location.contents:
            if self.args == ishere.key:
                self.msg("It is right here!\n")
                skip = 0

        if skip:
            for arg in self.caller.location.exits:
                matches = [obj for obj in arg.destination.contents if not obj.destination and self.args == obj.key]
                if matches:
                    self.msg("You sense it is %s. \n" % arg)
                    return
                else:
                    for mynxt in arg.destination.exits:
                        matches2 = [obj for obj in mynxt.destination.contents if not obj.destination and self.args == obj.key]
                        if matches2:
                            self.msg("You sense it is %s. \n" % arg)
                            return
                        else:
                            for mynxt2 in mynxt.destination.exits:
                                matches3 = [obj for obj in mynxt2.destination.contents if not obj.destination and self.args == obj.key]
                                if matches3:
                                    self.msg("You sense it is %s. \n" % arg)
                                    return
                                else:
                                    for mynxt3 in mynxt2.destination.exits:
                                        matches4 = [obj for obj in mynxt3.destination.contents if not obj.destination and self.args == obj.key]
                                        if matches4:
                                            self.msg("You sense it is %s. \n" % arg)
                                            return

                                        else:
                                            for mynxt4 in mynxt3.destination.exits:
                                                matches5 = [obj for obj in mynxt4.destination.contents if not obj.destination and self.args == obj.key]
                                                if matches5:
                                                    self.msg("You sense it is %s. \n" % arg)
                                                    return
                                            else:
                                                for mynxt5 in mynxt4.destination.exits:
                                                    matches6 = [obj for obj in mynxt5.destination.contents if not obj.destination and self.args == obj.key]
                                                    if matches6:
                                                        self.msg("You sense it is %s. \n" % arg)
                                                        return
                                                else:
                                                    self.msg("You don't sense anything.")
                                                    return