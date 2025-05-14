#!/usr/bin/env python3

import subprocess as sp


vowels = ["a", "A", "i", "I", "u", "U", "q", "Q", "L", "e", "E", "o", "O"]
consonants = ["k", "K", "g", "G", "f", "c", "C", "j", "J", "F", "t", "T", "d", "D", "N", "w", "W", "x", "X", "n", "p", "P", "b", "B", "m", "y", "r", "l", "v", "S", "R", "s", "h"]


def run_sm_command(command):
    """ """
    
    p = sp.Popen(command, stdout=sp.PIPE, shell=True)
    try:
        outs, errs = p.communicate()
        result = outs.decode('utf-8')
        st = "Success"
    except sp.TimeoutExpired:
        os.kill(p.pid)
        result = ""
        st = "Timeout"
    except Exception as e:
        result = ""
        st = "Error"

    return result, st


def get_morph(word, morph_binary_file):
    """ """

    command = "echo " + word + " | " + "lt-proc " + morph_binary_file
    
    try:
        result, status = run_sm_command(command)
    except Exception as e:
        result = ""
        status = "InputError"
    
#    if status == "Success":
#        result = (p.communicate()[0]).decode('utf-8')
    
    return result


def check_rules(first, second):
    """ """

    res = ""
    sandhi_name = ""
    sutra = ""
    cont = 1
    
    if first == "akRa" and second.startswith("Uhin"):
        res = "akROhin" + second[4:]
        sandhi_name = "vqxXi"
        sutra = "akRAxUhinyAmupasaMKyAnam (vA 3604)"
        cont = 0
    if first == "sva" and second.startswith("Irin"):
        res = "svErin" + second[4:]
        sandhi_name = "vqxXi"
        sutra = "svAxIreriNoH (vA 3606)"
        cont = 0
    if first == "sva" and second.startswith("IraH"):
        res = "svEraH" + second[4:]
        sandhi_name = "vqxXi"
        sutra = "svAxIreriNoH (vA 3606)"
        cont = 0
    if first == "sva" and second.startswith("IriN"):
        res = "svEriN" + second[4:]
        sandhi_name = "vqxXi"
        sutra = "svAxIreriNoH (vA 3606)"
        cont = 0
    if first == "pra" and second.startswith("Uh"):
        res = "proh" + second[2:]
        sandhi_name = "vqxXi"
        sutra = "prAxUhoDoDyeRERyeRu (vA 3605)"
        cont = 0
    if first == "pra" and second.startswith("UD"):
        res = "prOD" + second[2:]
        sandhi_name = "vqxXi"
        sutra = "prAxUhoDoDyeRERyeRu (vA 3605)"
        cont = 0
    if first == "pra" and second.startswith("eRy"):
        res = "prERy" + second[3:]
        sandhi_name = "vqxXi"
        sutra = "prAxUhoDoDyeRERyeRu (vA 3605)"
        cont = 0
    if first == "pra" and second.startswith("eR"):
        res = "prER" + second[2:]
        sandhi_name = "vqxXi"
        sutra = "prAxUhoDoDyeRERyeRu (vA 3605)"
        cont = 0
    if first == "pra" and second.startswith("qN"):
        res = "prArN" + second[2:]
        sandhi_name = "vqxXi"
        sutra = "pravawsawarakambalavasanArNaxaSAnAmqNe (vA 3608-9)"
        cont = 0
    if first == "pra" and second.startswith("qN"):
        res = "prArN" + second[2:]
        sandhi_name = "vqxXi"
        sutra = "pravawsawarakambalavasanArNaxaSAnAmqNe (vA 3608-9)"
        cont = 0
    elif first == "pra" and second.startswith("q"):
        res = "prAr" + second[1:]
        sandhi_name = "vqxXi"
        sutra = "upasargAxqwi XAwoH (6.1.91)"
        cont = 0
    else:
        pass
    
    if first == "vawsawara" and second.startswith("qN"):
        res = "vawsawarArN" + second[2:]
        sandhi_name = "vqxXi"
        sutra = "pravawsawarakambalavasanArNaxaSAnAmqNe (vA 3608-9)"
        cont = 0
    if first == "kambala" and second.startswith("qN"):
        res = "kambalArN" + second[2:]
        sandhi_name = "vqxXi"
        sutra = "pravawsawarakambalavasanArNaxaSAnAmqNe (vA 3608-9)"
        cont = 0
    if first == "vasana" and second.startswith("qN"):
        res = "vasanArN" + second[2:]
        sandhi_name = "vqxXi"
        sutra = "pravawsawarakambalavasanArNaxaSAnAmqNe (vA 3608-9)"
        cont = 0
    if first == "qNa" and second.startswith("qN"):
        res = "qNArN" + second[2:]
        sandhi_name = "vqxXi"
        sutra = "pravawsawarakambalavasanArNaxaSAnAmqNe (vA 3608-9)"
        cont = 0
    if first == "xaSa" and second.startswith("qN"):
        res = "xaSArN" + second[2:]
        sandhi_name = "vqxXi"
        sutra = "pravawsawarakambalavasanArNaxaSAnAmqNe (vA 3608-9)"
        cont = 0
    if first.endswith("o") and second == "yam":
        res = first[:-1] + "avyam"
        sandhi_name = "vAnwa"
        sutra = "vAnwo yi prawyaye (6.1.79)"
        cont = 0
    if first.endswith("O") and second == "yam":
        res = first[:-1] + "Avyam"
        sandhi_name = "vAnwa"
        sutra = "vAnwo yi prawyaye (6.1.79)"
        cont = 0
    if first == "go" and second.startswith("yUw"):
        res = "gavyUw" + second[3:]
        sandhi_name = "vAnwa"
        sutra = "aXvaparimANe ca (vA 3544)"
        cont = 0
    if first == "Saka" and second == "anXuH":
        res = "SakanXuH"
        sandhi_name = "pararUpa"
        sutra = "SakanXvAxiRu pararUpam vAcyam (vA 3632)"
        cont = 0
    if first == "karka" and second == "anXuH":
        res = "karkanXuH"
        sandhi_name = "pararUpa"
        sutra = "SakanXvAxiRu pararUpam vAcyam (vA 3632)"
        cont = 0
    if first == "kula" and second == "atA":
        res = "kulatA"
        sandhi_name = "pararUpa"
        sutra = "SakanXvAxiRu pararUpam vAcyam (vA 3632)"
        cont = 0
    if first == "hala" and second == "IRA":
        res = "karkanXuH"
        sandhi_name = "pararUpa"
        sutra = "SakanXvAxiRu pararUpam vAcyam (vA 3632)"
        cont = 0
    if first == "lAfgala" and second == "IRa":
        res = "lAfgalIRa"
        sandhi_name = "pararUpa"
        sutra = "SakanXvAxiRu pararUpam vAcyam (vA 3632)"
        cont = 0
    if first == "mArwa" and second == "aNdaH":
        res = "mArwaNdaH"
        sandhi_name = "pararUpa"
        sutra = "SakanXvAxiRu pararUpam vAcyam (vA 3632)"
        cont = 0
    if first == "sIman" and second == "anwaH":
        res = "sImanwaH"
        sandhi_name = "pararUpa"
        sutra = "sImanwaH keSaveSe (vA 3633)"
        cont = 0
    if first == "sAra" and second.startswith("aNdaH"):
        res = "sArafg"
        sandhi_name = "pararUpa"
        sutra = "sArafgaH paSupakRiNoH (gaNa sUwram 136)"
        cont = 0
    if first == "manas" and second == "IRA":
        res = "manIRA"
        sandhi_name = "pararUpa"
        sutra = "SakanXvAxiRu pararUpam vAcyam (vA 3632)"
        cont = 0
    if first == "pawaw" and second == "aFjaliH":
        res = "pawaFjaliH"
        sandhi_name = "pararUpa"
        sutra = "SakanXvAxiRu pararUpam vAcyam (vA 3632)"
        cont = 0
    if first[-1] in ["a", "A"] and second == "owuH":
        res = first[:-1] + second
        sandhi_name = "pararUpa"
        sutra = "owvoRTayoH samAse vA (vA 3634)"
        cont = 1
    if first[-1] in ["a", "A"] and second.startswith("oRT"):
        res = first[:-1] + second
        sandhi_name = "pararUpa"
        sutra = "owvoRTayoH samAse vA (vA 3634)"
        cont = 1
    if first == "kaH" and second == "kaH":
        res = "kaskaH"
        sandhi_name = "sakAra"
        sutra = "kaskAxiRu ca (8.3.48)"
        cont = 0
    if first == "kOwaH" and second == "kuwaH":
        res = "kOwaskuwaH"
        sandhi_name = "sakAra"
        sutra = "kaskAxiRu ca (8.3.48)"
        cont = 0
    if first == "kaH" and second == "kaH":
        res = "BrAwuRpuwraH"
        sandhi_name = "sakAra"
        sutra = "kaskAxiRu ca (8.3.48)"
        cont = 0
    if first == "SunaH" and second == "karNaH":
        res = "SunaskarNaH"
        sandhi_name = "sakAra"
        sutra = "kaskAxiRu ca (8.3.48)"
        cont = 0
    if first == "saxyaH" and second == "kAlaH":
        res = "saxyaskAlaH"
        sandhi_name = "sakAra"
        sutra = "kaskAxiRu ca (8.3.48)"
        cont = 0
    if first == "saxyaH" and second == "krIH":
        res = "saxyaskrIH"
        sandhi_name = "sakAra"
        sutra = "kaskAxiRu ca (8.3.48)"
        cont = 0
    if first == "sAxyaH" and second == "kaH":
        res = "sAxyaskaH"
        sandhi_name = "sakAra"
        sutra = "kaskAxiRu ca (8.3.48)"
        cont = 0
    if first == "kAMH" and second == "kAn":
        res = "kAMskAn"
        sandhi_name = "sakAra"
        sutra = "kaskAxiRu ca (8.3.48)"
        cont = 0
    if first == "sarpiH" and second == "kuNdikA":
        res = "sarpiRkuNdikA"
        sandhi_name = "sakAra"
        sutra = "kaskAxiRu ca (8.3.48)"
        cont = 0
    if first == "XanuH" and second == "kapAlam":
        res = "XanuRkapAlam"
        sandhi_name = "sakAra"
        sutra = "kaskAxiRu ca (8.3.48)"
        cont = 0
    if first == "bahiH" and second == "palam":
        res = "bahiRpalam"
        sandhi_name = "sakAra"
        sutra = "kaskAxiRu ca (8.3.48)"
        cont = 0
    if first == "barhiH" and second == "palam":
        res = "barhiRpalam"
        sandhi_name = "sakAra"
        sutra = "kaskAxiRu ca (8.3.48)"
        cont = 0
    if first == "yajuH" and second == "pAwram":
        res = "yajuRpAwram"
        sandhi_name = "sakAra"
        sutra = "kaskAxiRu ca (8.3.48)"
        cont = 0
    if first == "ayaH" and second == "kAnwaH":
        res = "ayaskAnwaH"
        sandhi_name = "sakAra"
        sutra = "kaskAxiRu ca (8.3.48)"
        cont = 0
    if first == "wamaH" and second == "kANdaH":
        res = "wamaskANdaH"
        sandhi_name = "sakAra"
        sutra = "kaskAxiRu ca (8.3.48)"
        cont = 0
    if first == "ayaH" and second == "kANdaH":
        res = "ayaskANdaH"
        sandhi_name = "sakAra"
        sutra = "kaskAxiRu ca (8.3.48)"
        cont = 0
    if first == "mexaH" and second == "piNdaH":
        res = "mexaspiNdaH"
        sandhi_name = "sakAra"
        sutra = "kaskAxiRu ca (8.3.48)"
        cont = 0
    if first == "BAH" and second == "karaH":
        res = "BAskaraH"
        sandhi_name = "sakAra"
        sutra = "kaskAxiRu ca (8.3.48)"
        cont = 0
    if first == "ahaH" and second == "karaH":
        res = "ahaskaraH"
        sandhi_name = "sakAra"
        sutra = "kaskAxiRu ca (8.3.48)"
        cont = 0
    if first == "namaH" and second[0] in ["k", "p"]:
        res = "namas" + second
        sandhi_name = "sakAra"
        sutra = "namaspurasorgawyoH (8.3.40)"
        cont = 0
    if first == "puraH" and second[0] in ["k", "p"]:
        res = "puras" + second
        sandhi_name = "sakAra"
        sutra = "namaspurasorgawyoH (8.3.40)"
        cont = 0
    if first == "wiraH" and second[0] in ["k", "p"]:
        res = "wiras" + second + ":wiraH " + second
        sandhi_name = "sakAra" + ":sawvaBAve"
        sutra = "wirasoZnyawarasyAm (8.3.42)" + ":wirasoZnyawarasyAm (8.3.42)"
        cont = 0
    if first == "apa" and second.startswith("q"):
        res = "apAr" + second[1:]
        sandhi_name = "vqxXi"
        sutra = "upasargAxqwi XAwoH(6.1.91)"
        cont = 0
    if first == "ava" and second.startswith("q"):
        res = "avAr" + second[1:]
        sandhi_name = "vqxXi"
        sutra = "upasargAxqwi XAwoH(6.1.91)"
        cont = 0
    if first == "upa" and second.startswith("q"):
        res = "upAr" + second[1:]
        sandhi_name = "vqxXi"
        sutra = "upasargAxqwi XAwoH(6.1.91)"
        cont = 0
    if first.endswith("pra") and second[0] in ["e", "o"]:
        res = first[:-3] + "pr" + second
        sandhi_name = "pararUpa"
        sutra = "efi pararUpam (6.1.94)"
        cont = 0
    if first.endswith("pa") and len(first) >= 3 and first[-3] in ["a", "A", "o", "u"] and second[0] in ["e", "o"]:
        res = first[:-2] + "p" + second
        sandhi_name = "pararUpa"
        sutra = "efi pararUpam (6.1.94)"
        cont = 0
    if first.endswith("a") and second.startswith("o") and second[1] in ["m", "z", "f", "F", "n", "N"]:
        res = first[:-1] + second
        sandhi_name = "pararUpa"
        sutra = "omAfoSca(6.1.95)"
        cont = 0
    if first == "go" and second[0] == "a":
        res = "go " + second + ":gavA" + second[1:]
        sandhi_name = "prakqwiBAva" + ":avafAxeSa"
        sutra = "omAfoSca(6.1.95)" + ":avaf sPotAyanasya(6.1.123)-> akaH savarNe xIrGaH (6.1.101)"
        cont = 1
    if first == "go" and second[0] in ["i", "I"]:
        res = "gave" + second[1:]
        sandhi_name = "avafAxeSa"
        sutra = "avaf sPotAyanasya(6.1.123)-> Ax guNaH (6.1.87)"
        cont = 0
    if first == "go" and second[0] in ["u", "U"]:
        res = "gavo" + second[1:]
        sandhi_name = "avafAxeSa"
        sutra = "avaf sPotAyanasya(6.1.123)-> Ax guNaH (6.1.87)"
        cont = 0
    if first == "go" and second[0] in ["q", "Q"]:
        res = "gavar" + second[1:]
        sandhi_name = "avafAxeSa"
        sutra = "avaf sPotAyanasya(6.1.123)-> Ax guNaH (6.1.87)"
        cont = 0
    if first == "go" and second[0] in ["L"]:
        res = "gaval" + second
        sandhi_name = "avafAxeSa"
        sutra = "avaf sPotAyanasya(6.1.123)-> Ax guNaH (6.1.87)"
        cont = 0
    if first == "go" and second[0] in ["e", "E"]:
        res = "gavE" + second
        sandhi_name = "avafAxeSa"
        sutra = "avaf sPotAyanasya(6.1.123)-> Ax guNaH (6.1.87)"
        cont = 0
    if first == "go" and second[0] in ["o", "O"]:
        res = "gavO" + second
        sandhi_name = "avafAxeSa"
        sutra = "avaf sPotAyanasya(6.1.123)-> Ax guNaH (6.1.87)"
        cont = 0
    if first == "go" and second.startswith("inxr"):
        res = "gavenxr" + second[4:]
        sandhi_name = "avafAxeSa"
        sutra = "inxre ca(6.1.124)-> Ax guNaH (6.1.87)"
        cont = 0
    if first[-1] in ["t", "T", "d", "D", "N"] and second == "nAm":
        res = first[:-1] + "NNAm"
        sandhi_name = "jaSwva-> RtuwvaniReXaH-> Nawva"
        sutra = "JalAM jaSoZnwe # (8.2.39)-> RtunA RtuH # (8.4.41)[Rtuwve prApwe]-> na paxAnwAttoranAm # (8.4.42)-> anAmnavawinagarINAmiwi vAcyam(vA 5016)-> yaroZnunAsikeZnunAsiko vA (8.4.45)-> prawyaye BARAyAm niwyam (vA 5017)"
        cont = 0
    if first[-1] in ["t", "T", "d", "D", "N"] and second == "navawi":
        res = first[:-1] + "NNAvawi"
        sandhi_name = "jaSwva-> RtuwvaniReXaH-> Nawva-> anunAsikawvam"
        sutra = "JalAM jaSoZnwe # (8.2.39)-> RtunA RtuH # (8.4.41)[Rtuwve prApwe]-> na paxAnwAttoranAm # (8.4.42)-> anAmnavawinagarINAmiwi vAcyam(vA 5016)-> yaroZnunAsikeZnunAsiko vA (8.4.45)"
        cont = 1
    if first[-1] in ["t", "T", "d", "D", "N"] and second.startswith("nagar"):
        res = first[:-1] + "NNagar" + second[5:]
        sandhi_name = "jaSwva-> RtuwvaniReXaH-> Nawva-> anunAsikawvam"
        sutra = "JalAM jaSoZnwe # (8.2.39)-> RtunA RtuH # (8.4.41)[Rtuwve prApwe]-> na paxAnwAttoranAm # (8.4.42)-> anAmnavawinagarINAmiwi vAcyam(vA 5016)-> yaroZnunAsikeZnunAsiko vA (8.4.45)"
        cont = 1
    if first in ["amI", "amU"]:
        res = first + " " + second
        sandhi_name = "prakqwiBAva"
        sutra = "axaso mAw(1.1.12)"
        cont = 0
    if first == "uw" and second.startswith("sWA"):
        res = "uwWA" + second[3:] + ":" + "uwWWA" + second[3:]
        sandhi_name = "pUrvasavarNaH->lopaH" + ":" + "pUrvasavarNaH->lopABAvaH"
        sutra = "uxaH sWAswamBoH pUrvasya (8.4.61)->Jaro Jari savarNe (8.4.65)" + ":" + "uxaH sWAswamBoH pUrvasya (8.4.61)->Jaro Jari savarNe (8.4.65)"
        cont = 0
    if first == "uw" and second.startswith("swamB"):
        res = "uwwamB" + second[3:] + ":" + "uwWwamB" + second[3:]
        sandhi_name = "pUrvasavarNaH->lopaH" + ":" + "pUrvasavarNaH->lopABAvaH"
        sutra = "uxaH sWAswamBoH pUrvasya (8.4.61)->Jaro Jari savarNe (8.4.65)" + ":" + "uxaH sWAswamBoH pUrvasya (8.4.61)->Jaro Jari savarNe (8.4.65)"
        cont = 0
    if first[-1] in ["k", "K", "g", "G"] and second[0] == "S" and second[1] in (vowels + "h" + "y" + "v" + "r"):
        res = first[:-1] + "kC" + second[1:]
        sandhi_name = "jaSwva->carwva->Cawva"
        sutra = "JalAM jaSoZnwe (8.2.39)->Kari ca (8.4.55)->SaSCoZti (8.4.63)"
        cont = 1
    if first[-1] in ["c", "C", "j", "J"] and second[0] == "S" and second[1] in (vowels + "h" + "y" + "v" + "r"):
        res = first[:-1] + "cC" + second[1:]
        sandhi_name = "jaSwva->carwva->Cawva"
        sutra = "JalAM jaSoZnwe (8.2.39)->Kari ca (8.4.55)->SaSCoZti (8.4.63)"
        cont = 1
    if first[-1] in ["t", "T", "d", "D"] and second[0] == "S" and second[1] in (vowels + "h" + "y" + "v" + "r"):
        res = first[:-1] + "tC" + second[1:]
        sandhi_name = "jaSwva->carwva->Cawva"
        sutra = "JalAM jaSoZnwe (8.2.39)->Kari ca (8.4.55)->SaSCoZti (8.4.63)"
        cont = 1
    if first[-1] in ["w", "W", "x", "X"] and second[0] == "S" and second[1] in (vowels + "h" + "y" + "v" + "r"):
        res = first[:-1] + "cC" + second[1:]
        sandhi_name = "jaSwva->Scuwva->carwva->Cawva"
        sutra = "JalAM jaSoZnwe (8.2.39)->swoH ScunA ScuH (8.4.40)->Kari ca (8.4.55)->SaSCoZti (8.4.63)"
        cont = 1
    if first[-1] in ["p", "P", "b", "B"] and second[0] == "S" and second[1] in (vowels + "h" + "y" + "v" + "r"):
        res = first[:-1] + "pC" + second[1:]
        sandhi_name = "jaSwva->carwva->Cawva"
        sutra = "JalAM jaSoZnwe (8.2.39)->Kari ca (8.4.55)->SaSCoZti (8.4.63)"
        cont = 1
    if first.endswith("n") and second[0] == "S" and second[1] in (vowels + ["h", "y", "v", "r"]):
        res = first[:-1] + "FC" + second[1:] + ":" + first[:-1] + "FcC" + second[1:]
        sandhi_name = "wugAgama->Scuwva->carwva->Cawva->lopaH" + ":" + "wugAgama->Scuwva->carwva->Cawva->lopABAvaH"
        sutra = "Si wuk (8.3.31)->swoH ScunA ScuH (8.4.40)->Kari ca (8.4.55)->SaSCoZti (8.4.63)->Jaro Jari savarNe (8.4.65)" + ":" + "Si wuk (8.3.31)->swoH ScunA ScuH (8.4.40)->Kari ca (8.4.55)->SaSCoZti (8.4.63)"
        cont = 1
    if first[-1] in ["k", "K", "g", "G"] and second[0] == "S" and second[1] in ("l" + "f" + "m" + "F", "N", "n"):
        res = first[:-1] + "kC" + second[1:] + ":" + first[:-1] + "kS" + second[1:]
        sandhi_name = "jaSwva->carwva->Cawva" + ":" + "jaSwva->carwva->CawvABAva"
        sutra = "JalAM jaSoZnwe (8.2.39)->Kari ca (8.4.55)->CawvamamIwi vAcyam (vA 5025)" + ":" + "JalAM jaSoZnwe (8.2.39)->Kari ca (8.4.55)"
        cont = 0
    if first[-1] in ["c", "C", "j", "J"] and second[0] == "S" and second[1] in ("l" + "f" + "m" + "F", "N", "n"):
        res = first[:-1] + "cC" + second[1:] + ":" + first[:-1] + "cS" + second[1:]
        sandhi_name = "jaSwva->carwva->Cawva" + ":" + "jaSwva->carwva->CawvABAva"
        sutra = "JalAM jaSoZnwe (8.2.39)->Kari ca (8.4.55)->CawvamamIwi vAcyam (vA 5025)" + ":" + "JalAM jaSoZnwe (8.2.39)->Kari ca (8.4.55)"
        cont = 0
    if first[-1] in ["t", "T", "d", "D"] and second[0] == "S" and second[1] in ("l" + "f" + "m" + "F", "N", "n"):
        res = first[:-1] + "tC" + second[1:] + ":" + first[:-1] + "tS" + second[1:]
        sandhi_name = "jaSwva->carwva->Cawva" + ":" + "jaSwva->carwva->CawvABAva"
        sutra = "JalAM jaSoZnwe (8.2.39)->Kari ca (8.4.55)->CawvamamIwi vAcyam (vA 5025)" + ":" + "JalAM jaSoZnwe (8.2.39)->Kari ca (8.4.55)"
        cont = 0
    if first[-1] in ["w", "W", "x", "X"] and second[0] == "S" and second[1] in ("l" + "f" + "m" + "F", "N", "n"):
        res = first[:-1] + "cC" + second[1:] + ":" + first[:-1] + "cS" + second[1:]
        sandhi_name = "jaSwva->Scuwva->carwva->Cawva" + ":" + "jaSwva->Scuwva->carwva->CawvABAva"
        sutra = "JalAM jaSoZnwe (8.2.39)->swoH ScunA ScuH (8.4.40)->Kari ca (8.4.55)->CawvamamIwi vAcyam (vA 5025)" + ":" + "JalAM jaSoZnwe (8.2.39)->swoH ScunA ScuH (8.4.40)->Kari ca (8.4.55)"
        cont = 0
    if first[-1] in ["p", "P", "b", "B"] and second[0] == "S" and second[1] in ("l" + "f" + "m" + "F", "N", "n"):
        res = first[:-1] + "pC" + second[1:] + ":" + first[:-1] + "pS" + second[1:]
        sandhi_name = "jaSwva->carwva->Cawva" + ":" + "jaSwva->carwva->CawvABAva"
        sutra = "JalAM jaSoZnwe (8.2.39)->Kari ca (8.4.55)->CawvamamIwi vAcyam (vA 5025)" + ":" + "JalAM jaSoZnwe (8.2.39)->Kari ca (8.4.55)"
        cont = 0
    if first.endswith("n") and second[0] in ["c", "C"] and second[1] in (vowels + "h" + "y" + "v" + "r"):
        res = first[:-1] + "zS" + second + ":" + first[:-1] + "MS" + second
        sandhi_name = "ruwva" + ":" + "ruwva"
        sutra = "naSCavyapraSAn (8.3.7)-> awrAnunAsikaH pUrvasya wu vA (8.3.2)-> KaravasAnayorvisarjanIyaH (8.3.15)-> visarjanIyasya saH (8.3.34)-> swoH ScunA ScuH (8.4.40)" + ":" + "naSCavyapraSAn (8.3.7)->anunAsikAw paroZnusvAraH (8.3.4)->KaravasAnayorvisarjanIyaH (8.3.15)->visarjanIyasya saH (8.3.34)->swoH ScunA ScuH (8.4.40)"
        cont = 0
    if first.endswith("n") and second[0] in ["t", "T"] and second[1] in (vowels + "h" + "y" + "v" + "r"):
        res = first[:-1] + "zR" + second + ":" + first[:-1] + "MR" + second
        sandhi_name = "ruwva" + ":" + "ruwva"
        sutra = "naSCavyapraSAn (8.3.7)->awrAnunAsikaH pUrvasya wu vA (8.3.2)->KaravasAnayorvisarjanIyaH (8.3.15)->visarjanIyasya saH (8.3.34)->RtunA RtuH (8.4.41)" + ":" + "naSCavyapraSAn (8.3.7)->anunAsikAw paroZnusvAraH (8.3.4)->KaravasAnayorvisarjanIyaH (8.3.15)->visarjanIyasya saH (8.3.34)->RtunA RtuH (8.4.41)"
        cont = 0
    if first.endswith("n") and second[0] in ["w", "W"] and second[1] in (vowels + "h" + "y" + "v" + "r"):
        res = first[:-1] + "zs" + second + ":" + first[:-1] + "Ms" + second
        sandhi_name = "ruwva" + ":" + "ruwva"
        sutra = "naSCavyapraSAn (8.3.7)->awrAnunAsikaH pUrvasya wu vA (8.3.2)->KaravasAnayorvisarjanIyaH (8.3.15)->visarjanIyasya saH (8.3.34)" + ":" + "naSCavyapraSAn (8.3.7)->anunAsikAw paroZnusvAraH (8.3.4)->KaravasAnayorvisarjanIyaH (8.3.15)->visarjanIyasya saH (8.3.34)"
        cont = 0
    if first == "praSAn" and second[0] in ["c", "C"] and second[1] in (vowels + "h" + "y" + "v" + "r"):
        res = "praSAF" + second
        sandhi_name = "ruwvaniReXa->Scuwva"
        sutra = "naSCavyapraSAn (8.3.7)-> swoH ScunA ScuH (8.4.40)"
        cont = 0
    if first == "praSAn" and second[0] in ["t", "T"] and second[1] in (vowels + "h" + "y" + "v" + "r"):
        res = "praSAN" + second
        sandhi_name = "ruwvaniReXa->Rtuwva"
        sutra = "naSCavyapraSAn (8.3.7)-> RtunA RtuH (8.4.41)"
        cont = 0
    if first == "praSAn" and second[0] in ["w", "W"] and second[1] in (vowels + "h" + "y" + "v" + "r"):
        res = "praSAn" + second
        sandhi_name = "ruwvaniReXa"
        sutra = "naSCavyapraSAn (8.3.7)"
        cont = 0
    if first == "nQn" and second.startswith("p"):
        res = "nQz><p" + second[1:] + ":" + "nQM><p" + second[1:] + ":" + "nQzHp" + second[1:] + ":" + "nQMHp" + second[1:] + ":" + "nQnp" + second[1:] 
        sandhi_name = "ruwva" + ":" + "ruwva" + ":" + "ruwva" + ":" + "ruwva" + ":" + "ruwvABAve"
        sutra = "nQnpe (8.3.10)->awrAnunAsikaH pUrvasya wu vA (8.3.2)->KaravasAnayorvisarjanIyaH (8.3.15)->kupvoH><ka><pO ca (8.3.37)" + ":" + "nQnpe (8.3.10)->anunAsikAw paroZnusvAraH (8.3.4)->KaravasAnayorvisarjanIyaH (8.3.15)->kupvoH><ka><pO ca (8.3.37)" + ":" + "nQnpe (8.3.10)->awrAnunAsikaH pUrvasya wu vA (8.3.2)->KaravasAnayorvisarjanIyaH (8.3.15)->visarjanIyasya saH (8.3.34)" + ":" + "nQnpe (8.3.10)->anunAsikAw paroZnusvAraH (8.3.4)->KaravasAnayorvisarjanIyaH (8.3.15)->visarjanIyasya saH (8.3.34)" + ":" + "nQnpe (8.3.10)"
        cont = 0
    if first == "kAn" and second == "kAn":
        res = "kAzskAn" + ":" + "kAMskAn"
        sandhi_name = "ruwva" + ":" + "ruwva"
        sutra = "kAnAmrediwe (8.3.12)->awrAnunAsikaH pUrvasya wu vA (8.3.2)->KaravasAnayorvisarjanIyaH (8.3.15)->saMpuMkAnAM so vakwavyaH (vA 4892)" + ":" + "kAnAmrediwe (8.3.12)->anunAsikAw paroZnusvAraH (8.3.4)->KaravasAnayorvisarjanIyaH (8.3.15)->saMpuMkAnAM so vakwavyaH (vA 4892)"
        cont = 0
    if first == "puM" and second[0] in ["k", "K", "c", "C", "t", "T", "w", "W", "p", "P"] and second[1] in (vowels + "h" + "y" + "v" + "r"):
        res = "puMs" + second + ":" + "puzs" + second
        sandhi_name = "ruwva" + ":" + "ruwva"
        sutra = "pumaH Kayyampare (8.3.6)->anunAsikAw paroZnusvAraH (8.3.4)->KaravasAnayorvisarjanIyaH (8.3.15)->saMpuMkAnAM so vakwavyaH (vA 4892)" + ":" + "pumaH Kayyampare (8.3.6)->awrAnunAsikaH pUrvasya wu vA (8.3.2)->KaravasAnayorvisarjanIyaH (8.3.15)->saMpuMkAnAM so vakwavyaH (vA 4892)"
        cont = 0
    if first.endswith("H") and second[0] in ["K", "P", "C", "T", "W", "c", "t", "w", "k", "p", "y", "S", "R", "s"] and second[1] in ["S", "R", "s"]:
        res = first + " " + second
        sandhi_name = "visarga"
        sutra = "Sarpare visarjanIyaH (8.3.35)"
        cont = 0
    if first.endswith("H") and second[1] in ["K", "P", "C", "T", "W", "c", "t", "w", "k", "p", "y", "S", "R", "s"] and second[0] in ["S", "R", "s"]:
        res = first[:-1] + " " + second + ":" + first + " " + second + ":" + first[:-1] + second
        sandhi_name = "visargalopaH" + ":" + "visargalopABAve" + ":" + "sawva"
        sutra = "Karpare Sari vA visargalopo vakwavyaH (vA 4906)" + ":" + "Karpare Sari vA visargalopo vakwavyaH (vA 4906)" + "visarjanIyasya saH (8.3.34)"
        cont = 0
    if first == "sam" and second == "rAt":
        res = "samrAt"
        sandhi_name = "mawva"
        sutra = "mo rAji samaH kvO (8.2.35)"
        cont = 0
    if first.endswith("m") and second.startswith("hm"):
        res = first + " " + second + ":" + first[:-1] + "M" + second
        sandhi_name = "mawva" + ":" + "anusvAraH"
        sutra = "he mapare vA (8.3.26)" + ":" + "moZnusvAraH (8.3.23)"
        cont = 0
    if first.endswith("m") and second[0] == "h" and second[1] in ["y", "v", "l"]:
        res = first[:-1] + "z " + second + ":" + first[:-1] + "M " + second
        sandhi_name = "anunAsika" + ":" + "anusvAraH"
        sutra = "yavalapare yavalA vewi vakwavyam (vA 4902)" + ":" + "moZnusvAraH (8.3.23)"
        cont = 0
    if first.endswith("m") and second.startswith("hn"):
        res = first[:-1] + "n " + second + ":" + first[:-1] + "M" + second
        sandhi_name = "nawva" + ":" + "anusvAraH"
        sutra = "na pare naH (8.3.27)" + ":" + "moZnusvAraH (8.3.23)"
        cont = 0
    if first in ["eRaH", "saH"] and second[0] in ["g", "G", "f", "c", "C", "j", "J", "F", "t", "T", "d", "D", "N", "w", "W", "x", "X", "n", "b", "B", "m", "y", "r", "l", "v", "h"]:
        res = first[:-1] + " " + second
        sandhi_name = "visargalopa"
        sutra = "ewawwaxoH sulopoZkoranaFsamAse hali (6.1.132)"
        cont = 0
    if first[-1] in ["a", "A"] and second.startswith("e") and second[1:] in ["wi", "Ri", "mi", "wA", "wArO", "wAraH", "wAsi", "wAsWaH", "wAsWa", "wAsmi", "wAsvaH", "wAsmaH", "Ryawi", "RyawaH", "Ryanwi", "Ryasi", "RyaWaH", "RyaWa", "RyAmi", "RyAvaH", "RyAmaH", "wu"]:
        res = first[:-1] + "E" + second[1:]
        sandhi_name = "vqxXi"
        sutra = "ewyeXawyUTsu (6.1.86)"
        cont = 0
    if first[-1] in ["a", "A"] and second.startswith("E") and second[1:] in ["w", "wAm", "H", "wam", "wa", "va", "ma", "Ryaw", "RyawAm", "Ryan", "RyaH", "Ryawam", "Ryawa", "Ryam", "RyAva", "RyAma"]:
        res = first[:-1] + "E" + second[1:]
        sandhi_name = "vqxXi"
        sutra = "ewyeXawyUTsu (6.1.86)"
        cont = 0
    if first[-1] in ["a", "A"] and second[0] in ["e", "E"] and second[1] == "X":
        res = first[:-1] + "EX" + second[2:]
        sandhi_name = "vqxXi"
        sutra = "ewyeXawyUTsu (6.1.86)"
        cont = 0
    if first[-1] in ["a", "A"] and second.startswith("Uha"):
        res = first[:-1] + "Oha" + second[2:]
        sandhi_name = "vqxXi"
        sutra = "ewyeXawyUTsu (6.1.86)"
        cont = 0
    if first == "ahan" and second.startswith("rUpa"):
        res = "aho " + second
        sandhi_name = "ruwva-> uwva-> guNa"
        sutra = "roZsupi (8.2.69)(prApwe) -> rUparAwri raWanwareRuruwvam vAcyam (vA 4847)-> haSi ca (6.1.114)-> Ax guNaH (6.1.87)"
        cont = 0
    
    if first == "ahan" and second.startswith("rAwr"):
        res = "aho " + second
        sandhi_name = "ruwva-> uwva-> guNa"
        sutra = "roZsupi (8.2.69)(prApwe) -> rUparAwri raWanwareRuruwvam vAcyam (vA 4847)-> haSi ca (6.1.114)-> Ax guNaH (6.1.87)"
        cont = 0
    if first == "ahan" and second.startswith("raWanwara"):
        res = "aho " + second
        sandhi_name = "ruwva-> uwva-> guNa"
        sutra = "roZsupi (8.2.69)(prApwe) -> rUparAwri raWanwareRuruwvam vAcyam (vA 4847)-> haSi ca (6.1.114)-> Ax guNaH (6.1.87)"
        cont = 0
    if first == "ahan" and second.startswith("pawi"):
        res = "ahar" + second + ":" + "ahaH " + second + ":" + "aha><" + second
        sandhi_name = "rePa" + ":" + "visarga" + ":" + "upaXmAnIya"
        sutra = "roZsupi (8.2.69)-> KaravasAnayorvisarjanIyaH (8.3.15) (prApwe)-> aharAxInAm pawyAxiRu vA rePaH (vA 4851)" + ":" + "roZsupi (8.2.69) -> KaravasAnayorvisarjanIyaH (8.3.15)-> kupvo><ka><pO ca (8.3.37)" + ":" + "roZsupi (8.2.69)->  KaravasAnayorvisarjanIyaH (8.3.15) -> kupvo><ka><pO ca (8.3.37)"
        cont = 0
    if first == "ahan" and second.startswith("gaNa"):
        res = "ahar" + second
        sandhi_name = "rePa"
        sutra = "roZsupi (8.2.69)"
        cont = 0
    if first == "ahan" and second.startswith("puwra"):
        res = "ahar" + second + ":" + "ahaH " + second + ":" + "aha><" + second
        sandhi_name = "rePa" + ":" + "visarga" + ":" + "upaXmAnIya"
        sutra = "roZsupi (8.2.69)-> aharAxInAm pawyAxiRu vA rePaH (vA 4851)" + ":" + "roZsupi (8.2.69)-> kupvo><ka><pO ca (8.3.37)" + ":" + "roZsupi (8.2.69)-> kupvo><ka><pO ca (8.3.37)"
        cont = 0
    
    if first == "gIr" and second.startswith("pawi"):
        res = "gIr" + second + ":" + "gIH " + second + ":" + "gI><" + second
        sandhi_name = "rePa" + ":" + "visarga" + ":" + "upaXmAnIya"
        sutra = "KaravasAnayorvisarjanIyaH (8.3.15)(prApwe) -> aharAxInAm pawyAxiRu vA rePaH (vA 4851)" + ":" + "KaravasAnayorvisarjanIyaH (8.3.15)-> kupvo><ka><pO ca (8.3.37)" + ":" + "KaravasAnayorvisarjanIyaH (8.3.15)-> kupvo><ka><pO ca (8.3.37)"
        cont = 0
    if first == "gIr" and second.startswith("gaNa"):
        res = "gIr" + second
        sandhi_name = "rePa"
        sutra = "roZsupi (8.2.69)"
        cont = 0
    if first == "gIr" and second.startswith("puwra"):
        res = "gIr" + second + ":" + "gIH " + second + ":" + "gI><" + second
        sandhi_name = "rePa" + ":" + "visarga" + ":" + "upaXmAnIya"
        sutra = "roZsupi (8.2.69)-> aharAxInAm pawyAxiRu vA rePaH (vA 4851)" + ":" + "roZsupi (8.2.69)-> kupvo><ka><pO ca (8.3.37)" + ":" + "roZsupi (8.2.69)-> kupvo><ka><pO ca (8.3.37)"
        cont = 0
    if first == "XUr" and second.startswith("pawi"):
        res = "XUr" + second + ":" + "XUH " + second + ":" + "XU><" + second
        sandhi_name = "rePa" + ":" + "visarga" + ":" + "upaXmAnIya"
        sutra = "roZsupi (8.2.69)-> KaravasAnayorvisarjanIyaH (8.3.15) (prApwe)-> aharAxInAm pawyAxiRu vA rePaH (vA 4851)" + ":" + "roZsupi (8.2.69) -> KaravasAnayorvisarjanIyaH (8.3.15)-> kupvo><ka><pO ca (8.3.37)" + ":" + "roZsupi (8.2.69)->  KaravasAnayorvisarjanIyaH (8.3.15) -> kupvo><ka><pO ca (8.3.37)"
        cont = 0
    if first == "XUr" and second.startswith("gaNa"):
        res = "XUr" + second
        sandhi_name = "rePa"
        sutra = "roZsupi (8.2.69)"
        cont = 0
    if first == "XUr" and second.startswith("puwra"):
        res = "XUr" + second + ":" + "XUH " + second + ":" + "XU><" + second
        sandhi_name = "rePa" + ":" + "visarga" + ":" + "upaXmAnIya"
        sutra = "roZsupi (8.2.69)-> aharAxInAm pawyAxiRu vA rePaH (vA 4851)" + ":" + "roZsupi (8.2.69)-> kupvo><ka><pO ca (8.3.37)" + ":" + "roZsupi (8.2.69)-> kupvo><ka><pO ca (8.3.37)"
        cont = 0
    
    if first == "ahan" and second == "ahaH":
        res = "aharahaH"
        sandhi_name = "rePa"
        sutra = "roZsupi (8.2.69)"
        cont = 0
    elif len(first) >= 2 and first[-2] in ["a", "A", "i", "u", "q"] and first[-1] in ["f", "N", "n"] and second[0] in vowels:
        res = first + first[-1] + second
        sandhi_name = "famudAgama"
        sutra = "famo hrasvAxaci famuNniwyam (8.3.32)"
        cont = 0
    elif len(first) >= 2 and first[-2] not in ["a", "A", "i", "u", "q"] and first[-1] in ["f", "N", "n"] and second[0] in vowels:
        res = first + second
        sandhi_name = "diPAlta"
        sutra = ""
        cont = 0
    else:
        pass

    if len(first) >= 2 and first[-2] in ["i", "I", "u", "U", "q", "Q", "L", "e", "E", "o", "O"] and first[1] == "H" and second[0] in (vowels + ["g", "G", "f", "j", "J", "F", "d", "D", "N", "x", "X", "n", "b", "B", "m", "y", "l", "v", "h"]):
        res = first[:-1] + "r" + second
        sandhi_name = "rePa"
        sutra = "sasajuRo ruH (8.2.66)"
        cont = 0
    
    if first == "eRaH" and second[0] in consonants:
        res = "eRa " + second
        sandhi_name = "visargalopa"
        sutra = "ewawwaxoH sulopoZkoranaFsamAse hali (6.1.132)"
        cont = 0
    elif first == "saH" and second[0] in consonants:
        res = "sa " + second
        sandhi_name = "visargalopa"
        sutra = "ewawwaxoH sulopoZkoranaFsamAse hali (6.1.132)"
        cont = 0
    elif first.endswith("aH") and second[0] in ["g", "G", "f", "j", "J", "F", "d", "D", "N", "x", "X", "n", "b", "B", "m", "y", "l", "v", "h"]:
        res = first[:-2] + "o " + second
        sandhi_name = "ruwva-> uwva-> guNa"
        sutra = "sasajuRo ruH (8.2.66)-> haSi ca (6.1.114)-> Ax guNaH (6.1.87)"
        cont = 0
    elif len(first) >= 2 and first[-2] in vowels and first[-1] == "H" and second[0] in ["w", "W"] and not second[1] in ["s", "S", "R"]:
        res = first[:-1] + "s" + second
        sandhi_name = "sawva"
        sutra = "visarjanIyasya saH (8.3.34)"
        cont = 0
    else:
        pass

    if len(first) >= 2 and first[-2] in vowels and first[-1] == "H" and second[0] in ["c", "C"]:
        res = first[:-1] + "S" + second
        sandhi_name = "sawva-> Scuwva"
        sutra = "visarjanIyasya saH (8.3.34)-> swoH ScunA ScuH (8.4.40)"
        cont = 0
    if len(first) >= 2 and first[-2] in vowels and first[-1] == "H" and second[0] in ["t", "T"]:
        res = first[:-1] + "R" + second
        sandhi_name = "sawva-> Rtuwva"
        sutra = "visarjanIyasya saH (8.3.34)-> RtunA RtuH (8.4.41)"
        cont = 0
    if first.endswith("AH") and second[0] in ["g", "G", "f", "j", "J", "F", "d", "D", "N", "x", "X", "n", "b", "B", "m", "y", "l", "v", "h"]:
        res = first[:-1] + " " + second
        sandhi_name = "ruwva-> yawva-> lopa"
        sutra = "sasajuRo ruH (8.2.66)-> BoBagoaGo apUrvasya yoZSi (8.3.17)-> hali sarveRAm (8.3.22)"
        cont = 0
    if first == "BoH" and second[0] in consonants:
        res = first[:-1] + "s" + second
        sandhi_name = ""
        sutra = "sasajuRo ruH (8.2.66)-> KaravasAnayorvisarjanIyaH (8.3.15)-> visarjanIyasya saH (8.3.34)"
        cont = 0
    if first == "BoH" and second[0] in vowels:
        res = first[:-1] + "y" + second + ":" + first[:-1] + " " + second
        sandhi_name = "sawva->yawva->laGuprayawnAxeSaH" + ":" + "sawva->yawva->laGuprayawnABAve yawvalopa"
        sutra = "sasajuRo ruH (8.2.66)->BoBagoaGo apUrvasyayoZSi (8.3.17)->vyorlaGuprayawnawaraH SAkatAyanasya (8.3.18)" + ":" + "sasajuRo ruH (8.2.66)->BoBagoaGo apUrvasyayoZSi (8.3.17)->owo gArgyasya (8.3.20)"
        cont = 0
    if first == "BagoH" and second[0] in consonants:
        res = first[:-1] + " " + second
        sandhi_name = "yawvalopaH"
        sutra = "sasajuRo ruH (8.2.66)->BoBagoaGo apUrvasyayoZSi (8.3.17)->hali sarveRAm (8.3.22)"
        cont = 0
    if first == "BagoH" and second[0] in vowels:
        res = first[:-1] + "y" + second + ":" + first[:-1] + " " + second
        sandhi_name = "sawva->yawva->laGuprayawnAxeSaH" + ":" + "sawva->yawva->laGuprayawnABAve yawvalopa"
        sutra = "sasajuRo ruH (8.2.66)->BoBagoaGo apUrvasyayoZSi (8.3.17)->vyorlaGuprayawnawaraH SAkatAyanasya (8.3.18)" + ":" + "sasajuRo ruH (8.2.66)->BoBagoaGo apUrvasyayoZSi (8.3.17)->owo gArgyasya (8.3.20)"
        cont = 0
    if first == "aGoH" and second[0] in consonants:
        res = first[:-1] + " " + second
        sandhi_name = "yawvalopaH"
        sutra = "sasajuRo ruH (8.2.66)->BoBagoaGo apUrvasyayoZSi (8.3.17)->hali sarveRAm (8.3.22)"
        cont = 0
    if first == "aGoH" and second[0] in vowels:
        res = first[:-1] + "y" + second + ":" + first[:-1] + " " + second
        sandhi_name = "sawva->yawva->laGuprayawnAxeSaH" + ":" + "sawva->yawva->laGuprayawnABAve yawvalopa"
        sutra = "sasajuRo ruH (8.2.66)->BoBagoaGo apUrvasyayoZSi (8.3.17)->vyorlaGuprayawnawaraH SAkatAyanasya (8.3.18)" + ":" + "sasajuRo ruH (8.2.66)->BoBagoaGo apUrvasyayoZSi (8.3.17)->owo gArgyasya (8.3.20)"
        cont = 0
    if first == "miwo" and second[0] in vowels:
        res = "miwo " + second
        sandhi_name = "pragqhyawva->prakqwiBAva"
        sutra = "ow (1.1.15)-> pluwapragqhyA aci niwyam (6.1.125)"
        cont = 0
    
    if first == "ho" and second[0] in vowels:
        res = "ho " + second
        sandhi_name = "pragqhyawva->prakqwiBAva"
        sutra = "ow (1.1.15)-> pluwapragqhyA aci niwyam (6.1.125)"
        cont = 0
    if first == "aho" and second[0] in vowels:
        res = "aho " + second
        sandhi_name = "pragqhyawva->prakqwiBAva"
        sutra = "ow (1.1.15)-> pluwapragqhyA aci niwyam (6.1.125)"
        cont = 0
    if first == "Aho" and second[0] in vowels:
        res = "Aho " + second
        sandhi_name = "pragqhyawva->prakqwiBAva"
        sutra = "ow (1.1.15)-> pluwapragqhyA aci niwyam (6.1.125)"
        cont = 0
    if first == "uwAho" and second[0] in vowels:
        res = "uwAho " + second
        sandhi_name = "pragqhyawva->prakqwiBAva"
        sutra = "ow (1.1.15)-> pluwapragqhyA aci niwyam (6.1.125)"
        cont = 0
    if first == "no" and second[0] in vowels:
        res = "no " + second
        sandhi_name = "pragqhyawva->prakqwiBAva"
        sutra = "ow (1.1.15)-> pluwapragqhyA aci niwyam (6.1.125)"
        cont = 0
    if first == "aWo" and second[0] in vowels:
        res = "aWo " + second
        sandhi_name = "pragqhyawva->prakqwiBAva"
        sutra = "ow (1.1.15)-> pluwapragqhyA aci niwyam (6.1.125)"
        cont = 0

    if first in ["a", "i", "u", "q", "L", "e", "E", "o", "O"] and second[0] in vowels:
        res = "miwo " + second
        sandhi_name = "pragqhyawva->prakqwiBAva"
        sutra = "nipAwa ekAjanAf (1.1.14)-> pluwapragqhyA aci niwyam (6.1.125)"
        cont = 0
    if first == "uF" and second == "iwi":
        res = "u iwi" + ":" + "Uz iwi" + ":" + "viwi"
        sandhi_name = "vikalpena pragqhyawva-> prakqwiBAva" + ":" + "vikalpena Uz AxeSa->pragqhyawva->prakqwiBAva" + ":" + "vikalpABAve yaN"
        sutra = "uFaH (1.1.17)-> pluwapragqhyA aci niwyam (6.1.125)" + ":" + "Uz (1.1.18)-> pluwapragqhyA aci niwyam (6.1.125)" + ":" + "iko yaNaci (6.1.77)"
        cont = 0
    if first == "kRi" and second.startswith("ya"):
        res = "kRayya" + second[2:] + ":" + "kReya" + second[2:]
        sandhi_name = "SakyArWe ayAxeSa nipAwana" + ":" + "SakyArWABAve guNa"
        sutra = "kRayyajayyO SakyArWe (6.1.81)" + ":" + "sArvaXAwukArXaXAwukayoH (7.3.84)"
        cont = 0
    if first == "ji" and second.startswith("ya"):
        res = "jayya" + second[2:] + ":" + "jeya" + second[2:]
        sandhi_name = "SakyArWe ayAxeSa nipAwana" + ":" + "SakyArWABAve guNa"
        sutra = "kRayyajayyO SakyArWe (6.1.81)" + ":" + "sArvaXAwukArXaXAwukayoH (7.3.84)"
        cont = 0
    if first == "krI" and second.startswith("ya"):
        res = "krayya" + second[2:] + ":" + "kreya" + second[2:]
        sandhi_name = "krayaNArhe ayAxeSa nipAwanam" + ":" + "krayaNArhABAve guNa"
        sutra = "krayyaswaxarWe (6.1.82)" + ":" + "sArvaXAwukArXaXAwukayoH (7.3.84)"
        cont = 0
    if first == "aXaH" and second.startswith("paxa"):
        res = "aXaspaxa" + second[4:] + ":" + "aXaH><paxa" + second[4:] + ":" + "aXaH paxa" + second[4:]
        sandhi_name = "samAse sawva" + ":" + "upaXmAnIya" + ":" + "visarga"
        sutra = "aXaSSirasI paxe (8.3.47)" + ":" + "kupvo ><ka ><pO ca (8.3.37)" + ":" + "kupvo ><ka ><pO ca (8.3.37)"
        cont = 0
    if first == "SiraH" and second.startswith("paxa"):
        res = "Siraspaxa" + second[4:] + ":" + "SiraH><paxa" + second[4:] + ":" + "SiraH paxa" + second[4:]
        sandhi_name = "samAse sawva" + ":" + "upaXmAnIya" + ":" + "visarga"
        sutra = "aXaSSirasI paxe (8.3.47)" + ":" + "kupvo ><ka ><pO ca (8.3.37)" + ":" + "kupvo ><ka ><pO ca (8.3.37)"
        cont = 0
    if first.endswith("iH") and second[0] in ["k", "K"]:
        res = first[:-2] + "iR" + second + ":" + first[:-2] + "i" + second + ":" + first[:-2] + "iH" + second
        sandhi_name = "sAmarWye Rawvam" + ":" + "RawvABAve jihvAmUlIya" + ":" + "RawvABAve visarga"
        sutra = "isusoH sAmarWye (8.3.44)" + ":" + "kupvo ><ka ><pO ca (8.3.37)" + ":" + "kupvo ><ka ><pO ca (8.3.37)"
        cont = 0
    if first.endswith("iH") and second[0] in ["p", "P"]:
        res = first[:-2] + "iR" + second + ":" + first[:-2] + "i" + second + ":" + first[:-2] + "iH" + second
        sandhi_name = "sAmarWye Rawvam" + ":" + "RawvABAve jihvAmUlIya" + ":" + "RawvABAve visarga"
        sutra = "isusoH sAmarWye (8.3.44)" + ":" + "kupvo ><ka ><pO ca (8.3.37)" + ":" + "kupvo ><ka ><pO ca (8.3.37)"
        cont = 0
    if first.endswith("uH") and second[0] in ["k", "K"]:
        res = first[:-2] + "uR" + second + ":" + first[:-2] + "u" + second + ":" + first[:-2] + "uH" + second
        sandhi_name = "sAmarWye Rawvam" + ":" + "RawvABAve jihvAmUlIya" + ":" + "RawvABAve visarga"
        sutra = "isusoH sAmarWye (8.3.44)" + ":" + "kupvo ><ka ><pO ca (8.3.37)" + ":" + "kupvo ><ka ><pO ca (8.3.37)"
        cont = 0
    if first.endswith("uH") and second[0] in ["p", "P"]:
        res = first[:-2] + "uR" + second + ":" + first[:-2] + "u" + second + ":" + first[:-2] + "uH" + second
        sandhi_name = "sAmarWye Rawvam" + ":" + "RawvABAve jihvAmUlIya" + ":" + "RawvABAve visarga"
        sutra = "isusoH sAmarWye (8.3.44)" + ":" + "kupvo ><ka ><pO ca (8.3.37)" + ":" + "kupvo ><ka ><pO ca (8.3.37)"
        cont = 0
    
    return res, sandhi_name, sutra, cont


def sandhi_based_on_morph(first, second, morph_binary_file):
    """ """
    
    res = ""
    sandhi_name = ""
    sutra = ""
    found = 0
    cont = 1
    
    first_morph = get_morph(first, morph_binary_file)
    second_morph = get_morph(second, morph_binary_file)
    if second[0] == "A" and "upasarga:Af" in second_morph:
        if first[-1] in ["a", "A"]:
            res = first[:-1] + second
            sandhi_name = "pararUpa"
            sutra = "omAfoSca(6.1.95)"
            cont = 0
    else:
        if first[-1] in ["I", "U", "e"]:
            first_morphs = first_morph.split("/")
            for mrph in first_morphs:
                if "vacanam:2" in mrph:
                    found = 1
        if found == 1:
            res = "*" + first + " " + second
            sandhi_name = "pragqhya"
            sutra = "IxUxexxvivacanam pragqhyam (1.1.11) -> pluwapragqhyA aci niwyam (6.1.125); " \
                   + first + " paxasya xvivacana viSleRaNam aXikqwya"
            cont = 1
    
    return 


def exception_rules(first, second, morph_binary_file, with_sutra=False):
    """ """

    if with_sutra:
        res, sandhi_name, sutra, cont = check_rules(first, second, morph_binary_file)
    else:
        res, sandhi_name, sutra, cont = check_rules(first, second)
    
    return res, sandhi_name, sutra, cont
