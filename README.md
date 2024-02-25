# 6502-Emulator
A MOS 6502 emulator written in C

# Introduction
The MOS 6502 is one of the most influential chips to home entertainment computing in the 1980s. Machines like the Nintendo Entertainment System, Commodore 64, Apple II, Atari 2600, and more, utlilized this
chip to deliver hundreds of thousands of hours of content and memories. While many emulators for the individual systems exist, such as NESTopia for the NES, or VICE for the Commodore 64, this project strives to teach us, the developers, more about the system itself. While a goal of this project is to present it in a class setting, the primary, most important goal, is preserving old architectures in modern code, such that we may never lose the systems we grew up on to the ever increasing technologies of our generation.

## Architecture Overview and Goals

In order for this project to be considered complete, there will be multiple moving parts. I have separated them into two categories: _essential_ and _stretch_ goals. Essential goals are ones that are required to be completed by the due date for requirements of our class. Stretch goals are those that would make this emulator product ready and complete. 

Essential goals include:
- A library of C functions that, when fed single lines of MOS 6502 machine language instructions, output the desired result of _that instruction_
- A functioning assembler that takes in lines of human readable instructions and, parsing line by line (by lookup table or otherwise) parses the instructions into machine code. 

These are the essential parts of the project, such that if these two are done, the only remaining work to do is build the bridge between the assembled machine language and the C functions. I think if we have that working by project time, we should be well on our way to meet the requirements. To facilitate an ease of teamwork, these two sections will act as if the other is a black box, outputting only what the specific section of the project needs to so that the other section can understand and process it. 

Stretch goals include:
- A bridge between both 