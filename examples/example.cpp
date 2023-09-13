// Saves the current state to a file following the xyz-standard
// (see // http://en.wikipedia.org/wiki/XYZ_file_format)
void IO::saveState(System &system)
{
  if(file.is_open()) {
    file << system.atoms().size() << endl;
    file << endl;
    for(Atom *atom : system.atoms()) {
      vec3 p = atom->position;
      file <<
	"H " << p.x() << " " << p.y() << " " << p.z() << endl;
    }
  }
}
