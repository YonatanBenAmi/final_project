import speech_recognition as sr
from torch.ao.quantization.pt2e.duplicate_dq_pass import logger

from logger.logger import Logger

class STT:
    r = sr.Recognizer()
    logger = Logger.get_logger()

    def convert_audio_to_text(self, path):
        path = f"{path}"

        with sr.AudioFile(path) as source:
            audio = self.r.record(source)
            audio_content = self.r.recognize_google(audio)
            self.logger.info(f"Path: {path} - Audio Content: {audio_content}")
            return audio_content
    def add_audio_content(self, metadata:dict, audio_path:r"str")->dict:
        metadata["Audio content"] = self.convert_audio_to_text(audio_path)
        return metadata

    def add_for_all_the_metadata(self, list_metadata:list)->list:
        list_full_metadata = []
        for metadata in list_metadata:
            self.logger.info("Converting audio to text...")
            list_full_metadata.append(self.add_audio_content(metadata, metadata["Path"].encode('unicode_escape').decode()))
        return list_full_metadata


