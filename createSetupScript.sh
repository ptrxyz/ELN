for foldername in $(python3 scripts/parseYML.py read --collect configFileStructure.yml folders.item); do
    echo "mkdir -p shared/eln/${foldername}" >> setup.sh; \
done
echo "mkdir -p shared/eln/config" >> setup.sh

chmod +x setup.sh
