# Align Armature Bones Script

## Overview
This script aligns the bones of a selected armature to match those of another armature based on bone names. It modifies position, rotation, and scale to ensure accurate alignment.

## Installation
1. Open Blender.
2. Open the Scripting workspace.
3. Create a new script and paste the provided Python code.
4. Save the script with a `.py` extension.

## Usage
1. **Select two armatures:**
   - First, select the armature you want to align (source).
   - Then, select the reference armature (target) as the active object.
2. **Run the script:**
   - Open the Scripting workspace in Blender.
   - Load and execute the script.
3. The script will align all bones in the selected armature that have matching names in the active armature.

## Notes
- Ensure both objects are armatures.
- The script works in Edit Mode to modify bone positions.
- Only bones with matching names in both armatures will be aligned.

## Troubleshooting
- If the script does nothing, verify that both selected objects are armatures.
- Ensure you have selected exactly two armatures, with the reference armature set as the active object.

## License
This script is provided as-is, without warranty. Feel free to modify and use it in your projects!

