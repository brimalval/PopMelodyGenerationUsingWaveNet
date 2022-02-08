class MIDINote:

    def __init__(self, note, duration_type, length):
        self.note = note
        self.duration_type = duration_type
        self.length = length
        self.as_map = {
            "note": note,
            "duration_type": duration_type,
            "length": length
        }
